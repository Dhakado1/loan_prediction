import joblib
from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# Load model
model = joblib.load('final_model.joblib')

@app.route('/')
def home():
    return render_template('index.html', form_data=None)

@app.route('/predict', methods=['POST'])
def predict():
    form_data = request.form  # store submitted values

    user_name = form_data['Name']

    data = {
        'Gender': form_data['Gender'],
        'Married': form_data['Married'],
        'Dependents': form_data['Dependents'],
        'Education': form_data['Education'],
        'Self_Employed': form_data['Self_Employed'],
        'ApplicantIncome': float(form_data['ApplicantIncome']),
        'CoapplicantIncome': float(form_data['CoapplicantIncome']),
        'LoanAmount': float(form_data['LoanAmount']),
        'Loan_Amount_Term': float(form_data['Loan_Amount_Term']),
        'Credit_History': float(form_data['Credit_History']),
        'Property_Area': form_data['Property_Area']
    }

    df = pd.DataFrame([data])
    pred = model.predict(df)[0]

    if pred == 1:
        result = f"Congratulations {user_name}, your loan is Approved."
    else:
        result = f"Sorry {user_name}, your loan is Rejected."

    return render_template("index.html",
                           prediction=result,
                           form_data=form_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
