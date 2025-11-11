import joblib
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load model using joblib
model = joblib.load('final_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = {
        'Gender': request.form['Gender'],
        'Married': request.form['Married'],
        'Dependents': request.form['Dependents'],
        'Education': request.form['Education'],
        'Self_Employed': request.form['Self_Employed'],
        'ApplicantIncome': float(request.form['ApplicantIncome']),
        'CoapplicantIncome': float(request.form['CoapplicantIncome']),
        'LoanAmount': float(request.form['LoanAmount']),
        'Loan_Amount_Term': float(request.form['Loan_Amount_Term']),
        'Credit_History': float(request.form['Credit_History']),
        'Property_Area': request.form['Property_Area']
    }

    input_data = pd.DataFrame([data])
    prediction = model.predict(input_data)[0]

    result = "✅ Loan Approved" if prediction == 1 else "❌ Loan Rejected"
    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
