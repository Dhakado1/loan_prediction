🚀 Loan Approval Prediction System

A lightweight Machine Learning web app that predicts whether a loan should be approved or rejected based on user-entered financial and personal details.
Built with Flask, scikit-learn, and a clean HTML/CSS UI.

⭐ What This App Can Do

Predict loan approval instantly

Simple, responsive web interface

Works with a trained Random Forest model

Clean backend (Flask) + frontend (HTML/CSS)

Easy to deploy on Render

🧠 Tech Used

Python, Flask

pandas, numpy

scikit-learn

joblib

HTML / CSS

📂 Project Layout
Loan_Prediction_Project/
│── app.py
│── final_model.joblib
│── requirements.txt
│
├── templates/
│   └── index.html
└── static/
    └── style.css

▶️ Run Locally
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py


Open:

http://127.0.0.1:5000/

📊 About the Model

Trained on key features like:

Applicant Income

Co-applicant Income

Loan Amount

Credit History

Property Area

Education & Employment

Final model: Random Forest Classifier (best accuracy).

🔮 Future Add-ons

Admin Dashboard

Better UI with Bootstrap

Loan EMI calculator

Database storage

👨‍💻 Developer

Vikas Dhakad
B.Tech — Computer Science Engineering
