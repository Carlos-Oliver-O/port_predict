# 🚢 🇺🇸 Predict the delay - Flask Web App 🇺🇸

This project is a web application developed with Flask for Xnova International that predicts the delay in the delivery of shipments in the USA. The prediction is based on a Machine Learning model trained with historical data and processed through a preprocessing pipeline.

## ✨ Features

- 📦 Prediction of delays in cargo delivery.
- 🕒 Classification of delays into three categories: up to 10 days, 10 to 20 days and more than 20 days.
- 🖥️ Simple and easy to use web interface.

## 🛠️ Requirements

-Python 3.7+
- Flask
- joblib
- pandas
- scikit-learn
- xgboost

## 📥 Installation

1. Clone the repository:
 ```bash
 git clone https://github.com/tuusuario/predict-cargo-delay.git
 cd predict-cargo-delay
 ```

2. Create a virtual environment and activate the environment:
 ```bash
 python -m venv venv
 source venv/bin/activate # On Windows use `venv\Scripts\activate`
 ```

3. Install the dependencies:
 ```bash
 pip install -r requirements.txt
 ```

4. Run the Flask application:
 ```bash
 python app.py
 ```

5. Open your browser and go to `http://127.0.0.1:5000`.

## 📝 Usage

1. Enter the required data in the web form:
 - 🏢 Consignee address
 - 🚚 Carrier SASC code
 - ⚓ Charging port
 - 🚢 Download port
 - 📅 Year, month and day of the estimated arrival date

2. Click the prediction button to see the result:
 - **0**: The delay is up to 10 days.
 - **1**: The delay is 10 to 20 days.
 - **2**: The delay is more than 20 days.

## 📂 Project Structure

```plaintext
predict-cargo-delay/
│
├── app.py # Main file of Flask application
├── model.pkl # Pre-trained Machine Learning model
├── templates/
│ └── index.html # HTML template for the web interface
├── requirements.txt # Requirements file for dependencies
└── README.md # README file with project information
```

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

Be sure to replace `youruser` with your GitHub username and make any other necessary settings specific to your project. This README file now includes emojis and specifies that transactions are from the USA, which provides an attractive visual touch and additional clarity.
