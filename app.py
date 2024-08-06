from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Cargar el modelo XGBoost entrenado
with open('best_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Cargar el LabelEncoder y el Scaler
with open('label_encoders.pkl', 'rb') as f:
    label_encoders = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Ruta para mostrar el formulario HTML
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos del formulario
        consignee_address = request.form['consignee_address']
        product_desc = request.form['product_desc']
        carrier_sasc_code = request.form['carrier_sasc_code']
        inbond_type = float(request.form['inbond_type'])  # Convertir a float si es necesario
        loading_port = request.form['loading_port']
        unloading_port = request.form['unloading_port']
        container_type = request.form['container_type']

        # Crear un DataFrame con los datos del formulario
        data = {
            'consignee_address': [consignee_address],
            'product_desc': [product_desc],
            'carrier_sasc_code': [carrier_sasc_code],
            'inbond_type': [inbond_type],
            'loading_port': [loading_port],
            'unloading_port': [unloading_port],
            'container_type': [container_type]
        }
        df = pd.DataFrame(data)

        # Aplicar transformaciones con LabelEncoder y Scaler
        df_encoded = df.copy()
        df_encoded['consignee_address'] = label_encoders['consignee_address'].transform(df['consignee_address'])
        df_encoded['product_desc'] = label_encoders['product_desc'].transform(df['product_desc'])
        df_encoded['carrier_sasc_code'] = label_encoders['carrier_sasc_code'].transform(df['carrier_sasc_code'])
        df_encoded['loading_port'] = label_encoders['loading_port'].transform(df['loading_port'])
        df_encoded['unloading_port'] = label_encoders['unloading_port'].transform(df['unloading_port'])
        df_encoded['container_type'] = label_encoders['container_type'].transform(df['container_type'])
        
        # Asegurar que inbond_type sea numérico y escalarlo si es necesario
        df_encoded['inbond_type'] = df_encoded['inbond_type'].astype(float)
        
        # Escalar los datos
        df_scaled = pd.DataFrame(scaler.transform(df_encoded), columns=df_encoded.columns)

        # Hacer la predicción
        prediction = model.predict(df_scaled)  # Asumiendo que 'model' es un objeto XGBoost entrenado correctamente

        return f'Predicción: {prediction}'
    
    except Exception as e:
        return f'Error en predicción: {str(e)}'

if __name__ == '__main__':
    app.run(debug=True)
