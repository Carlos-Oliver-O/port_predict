from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Cargar el pipeline desde el archivo pickle
pipeline = joblib.load('pipeline_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Obtener los datos del formulario
    data = {
        'consignee_address': request.form['consignee_address'],
        'carrier_sasc_code': request.form['carrier_sasc_code'],
        'loading_port': request.form['loading_port'],
        'unloading_port': request.form['unloading_port'],
        'estimate_arrival_date_year': int(request.form['estimate_arrival_date_year']),
        'estimate_arrival_date_month': int(request.form['estimate_arrival_date_month']),
        'estimate_arrival_date_day': int(request.form['estimate_arrival_date_day']),
    }
    
    # Convertir los datos a un DataFrame
    df = pd.DataFrame([data])
    
    # Hacer la predicción
    prediction = pipeline.predict(df)[0]
    
    # Mapear las predicciones a categorías
    if prediction == 0:
        delay_category = 'Hasta 10 días'
    elif prediction == 1:
        delay_category = 'De 10 a 20 días'
    elif prediction == 2:
        delay_category = 'Más de 20 días'
    else:
        delay_category = 'Desconocido'
    
    # Retornar el resultado como JSON
    return jsonify({'prediction': delay_category})

if __name__ == '__main__':
    app.run(debug=True)
