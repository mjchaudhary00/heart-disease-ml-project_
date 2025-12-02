❤️ Heart Disease Prediction using Machine Learning

Educational Project – Not for Clinical Use

This project demonstrates an end-to-end Machine Learning pipeline for predicting heart disease risk using a synthetic real-world–style dataset of 30,000+ patients.
It includes data preprocessing, model training, evaluation, interpretability (SHAP), and deployment-ready structure.

📁 Project Structure
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
│
└── README.md

📊 Dataset Summary

The dataset contains 30,000 synthetic patient records with clinically relevant features:

Age

Sex

Chest Pain Type

Resting Blood Pressure

Cholesterol

Fasting Blood Sugar

Resting ECG

Maximum Heart Rate

Exercise-Induced Angina

Oldpeak (ST Depression)

ST Slope

BMI

Smoking

Diabetes

Family History

Physical Activity Level

Alcohol Use

Hypertension

Heart Disease (Target)

Note: Dataset is synthetic and used for educational purposes only.

🧠 Machine Learning Pipeline
✔ Data preprocessing

Train/Validation/Test split

Standard scaling

One-Hot Encoding for categorical variables

Passthrough for binary features

Pipelines for reproducibility

✔ Models trained

Logistic Regression

Random Forest

XGBoost

LightGBM

MLP Classifier

Stacking Ensemble (LR + RF + XGB)

✔ Metrics used

Accuracy

ROC-AUC

PR-AUC

Precision, Recall, F1

Calibration

🏆 Best Model: XGBoost

Example performance (replace with your real values):

Model	ROC-AUC	PR-AUC	Accuracy
Logistic Regression	0.87	0.62	0.80
Random Forest	0.92	0.70	0.85
XGBoost (Best)	0.94	0.76	0.87
LightGBM	0.93	0.74	0.86
MLP	0.89	0.66	0.82
Stacking Ensemble	0.95	0.77	0.88

(Values are example placeholders — replace with your notebook outputs.)

📈 Visualizations Included
✔ ROC Curve

✔ Precision-Recall Curve

✔ Random Forest Feature Importance

✔ XGBoost Feature Importance

✔ SHAP Summary (Global Interpretability)

✔ Decision Tree Visualization

🧩 Model Interpretability (Important for Healthcare)

Key insights from Random Forest + SHAP analysis:

Oldpeak is a major risk driver

Age increases risk almost linearly

Cholesterol and Resting BP contribute strongly

Exercise Angina and Max Heart Rate influence decision boundaries

SHAP summary plot shows clinically meaningful patterns

🚀 Deployment (API Ready)

API is built using FastAPI.

Run API locally:

uvicorn api.app:app --reload


Endpoint:

POST /predict


Request body example:

{
  "age": 54,
  "sex": 1,
  "cholesterol": 240,
  "max_hr": 150,
  "oldpeak": 1.5,
  "smoking": 0
}

⚠️ Ethical Disclaimer

This project is strictly educational.
The model must NOT be used for diagnosis, treatment, or clinical decision-making.
Synthetic data is used — no real patients involved.

📌 Future Improvements

Add probability calibration (Platt/Isotonic)

Fairness testing across demographic groups

Hyperparameter tuning with Optuna

Deployment via Streamlit or HuggingFace Spaces

Convert API into a full app (UI + backend)

👤 Author

Mehul J. Chaudhary (Mj)
AI-powered Epidemiology Expert
Data Analyst | ML Engineer
India