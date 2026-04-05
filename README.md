# 📊 Customer Churn Prediction System

## 🚀 Overview

This project is an end-to-end Machine Learning application that predicts whether a customer is likely to churn. It covers the complete ML lifecycle including data preprocessing, model training, evaluation, and deployment using FastAPI and Streamlit for real-time predictions.

---

## 🎯 Key Features

* Real-time churn prediction
* Confidence score with risk categorization (Low / Medium / High)
* Interactive UI using Streamlit
* REST API using FastAPI
* Model deployment on Render

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** FastAPI
* **ML Libraries:** Scikit-learn, Pandas, NumPy
* **Model Storage:** Joblib
* **Deployment:** Render

---

## 📂 Project Structure

```
├── app.py                # Streamlit frontend
├── server.py            # FastAPI backend
├── model.pkl            # Trained ML model
├── scaler.pkl           # Feature scaler
├── customer_churn_data.csv
├── notebook.ipynb       # Training & experimentation
├── requirements.txt
└── runtime.txt
```

---

## 🔬 Machine Learning Workflow

### 1. Data Loading

* Loaded dataset using Pandas
* Checked structure, columns, and data types

### 2. Data Preprocessing

* Converted categorical feature:

  * Gender → 0 (Male), 1 (Female)
* Selected important features:

  * Age
  * Gender
  * Tenure
  * Monthly Charges

### 3. Feature Scaling

* Applied **StandardScaler**
* Saved scaler as `scaler.pkl`

### 4. Train-Test Split

* Split data into training and testing sets (80/20)

### 5. Model Training

Trained multiple models:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

---

## 📊 Model Evaluation & Selection

### 🔍 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score

### 📈 Model Comparison

| Model               | Accuracy | Precision | Recall | F1-Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | ~0.82    | ~0.80     | ~0.78  | ~0.79    |
| Decision Tree       | ~0.78    | ~0.76     | ~0.75  | ~0.75    |
| Random Forest       | ~0.87    | ~0.85     | ~0.83  | ~0.84    |

---

### 🏆 Best Model

* **Random Forest Classifier** selected as final model
* Achieved highest accuracy and balanced performance
* Handles non-linearity and reduces overfitting

---

### 🎯 Final Accuracy

> **~87% Accuracy**

---

## ⚙️ How It Works

1. User inputs data in Streamlit UI
2. Data is sent to FastAPI backend
3. Backend:

   * Converts input to numerical format
   * Applies scaler
   * Sends data to model
4. Model returns:

   * Prediction (Churn / Not Churn)
   * Confidence score
5. UI displays result with risk level

---

## 📡 API Endpoint

### POST `/predict`

#### Request:

```json
{
  "age": 30,
  "gender": "male",
  "tenure": 10,
  "monthly_charges": 75
}
```

#### Response:

```json
{
  "prediction": 1,
  "label": "Churn",
  "confidence": 0.85
}
```

---

## ▶️ Run Locally

### Install dependencies

```
pip install -r requirements.txt
```

### Start backend

```
uvicorn server:app --reload
```

### Start frontend

```
streamlit run app.py
```

---

## 🌐 Deployment

* Backend deployed on Render
* Frontend connected via API

---

## 📌 Future Improvements

* Add more features (contract type, payment method)
* Hyperparameter tuning (GridSearchCV)
* Improve accuracy
* Add analytics dashboard


