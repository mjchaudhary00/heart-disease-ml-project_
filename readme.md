❤️ Heart Disease Prediction — End-to-End Machine Learning Project

Educational Project • Not for Medical Use

This project demonstrates a complete machine learning workflow for predicting the risk of heart disease using a synthetic real-world dataset of 30,000+ records.
It includes data preprocessing, model benchmarking, interpretability (SHAP), and a deployment-ready API.

📂 Project Structure
heart-disease-ml-project/
│
├── notebooks/
│   └── heart_disease_project.ipynb
│
├── data/
│   └── heart_disease_synthetic_30000.xlsx
│
├── models/
│   └── best_model_xgboost.pkl
│
├── images/
│   ├── roc_curves.png
│   ├── pr_curves.png
│   ├── rf_feature_importance_top20.png
│   ├── xgb_feature_importance.png
│   ├── shap_summary_xgb.png
│   └── decision_tree_visual.png
│
├── api/
│   └── app.py
│
├── requirements.txt
└── README.md

🧠 Project Overview
✔ Dataset

30,000+ synthetic patient records with features such as:

Demographics (age, sex)

Clinical measures (BP, cholesterol, oldpeak)

ECG results

Lifestyle factors (smoking, alcohol, activity level)

Medical history (diabetes, hypertension, family history)

heart_disease (target)

✔ ML Pipeline

Preprocessing using ColumnTransformer

Train/validation split

Baseline → advanced models

Probability calibration

SHAP explainability

Feature importance plots

API-ready model export

🏆 Model Performance (replace with your results)
Model	ROC-AUC	PR-AUC	Accuracy
Logistic Regression	0.87	0.62	0.80
Random Forest	0.92	0.70	0.85
XGBoost (Best)	0.94	0.76	0.87
LightGBM	0.93	0.74	0.86
Stacking Ensemble	0.95	0.77	0.88
📈 Visual Results
ROC Curve

Precision-Recall Curve

Random Forest Feature Importance

XGBoost Feature Importance

SHAP Summary

Decision Tree

🧩 Interpretability Insights (SHAP)

Oldpeak, Age, Cholesterol, Max HR, Exercise Angina are strong predictors

Consistent with clinical knowledge

Improves trust + transparency

🚀 API Deployment (FastAPI)

Run API locally:

uvicorn api.app:app --reload


Predict endpoint:

POST /predict


Example input:

{
  "age": 54,
  "sex": 1,
  "cholesterol": 240,
  "max_hr": 150,
  "oldpeak": 1.5,
  "smoking": 0
}

⚠️ Limitations

Synthetic dataset

Not medically validated

For learning and demonstration only

Should not be used for diagnosis

👤 Author — Mehul “Mj” Chaudhary

AI-powered Epidemiology Expert
Data Scientist | ML Engineer | Health Analytics
