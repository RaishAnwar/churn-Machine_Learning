# churn-Machine_Learning

# 📊 Customer Churn Prediction System

## 🚀 Overview

This project is an end-to-end Machine Learning pipeline designed to predict customer churn. It includes data preprocessing, model training, evaluation, and deployment using FastAPI and Streamlit for real-time predictions.

---

## 🎯 Key Highlights

* Built a complete ML pipeline from raw data to deployment
* Implemented feature preprocessing and scaling
* Trained and compared multiple classification models
* Deployed model using FastAPI (REST API)
* Integrated frontend using Streamlit

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** FastAPI
* **ML Libraries:** Scikit-learn, NumPy, Pandas
* **Model Serialization:** Joblib
* **Deployment:** Render

---

## 📂 Project Structure

```id="l3cs85"
├── app.py                # Streamlit frontend
├── server.py            # FastAPI backend
├── model.pkl            # Trained ML model
├── scaler.pkl           # Feature scaler
├── customer_churn_data.csv
├── notebook.ipynb       # Model training & experimentation
├── requirements.txt
└── runtime.txt
```

---

## 🔬 Machine Learning Workflow (Notebook Steps)

### 1. Data Loading

* Loaded customer dataset using Pandas
* Inspected dataset shape, columns, and data types

### 2. Data Cleaning

* Checked for missing values
* Removed/handled null values (if any)
* Ensured correct data types

### 3. Exploratory Data Analysis (EDA)

* Analyzed distribution of features
* Observed churn patterns
* Identified important variables affecting churn

### 4. Feature Engineering

* Converted categorical feature:

  * Gender → Numerical (0 / 1)
* Selected relevant features:

  * Age
  * Gender
  * Tenure
  * Monthly Charges

---

### 5. Feature Scaling

* Applied **StandardScaler** to normalize data
* Saved scaler using Joblib (`scaler.pkl`)

---

### 6. Train-Test Split

* Split dataset into training and testing sets
* Ensured proper distribution of target variable

---

### 7. Model Training

Trained multiple classification models:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier

---

### 8. Model Evaluation

Evaluated models using:

* Accuracy
* Precision
* Recall
* F1-score

Selected the best-performing model based on performance metrics

---

### 9. Model Saving

* Saved final model using Joblib (`model.pkl`)
* Saved scaler for consistent preprocessing

---

## ⚙️ How It Works (End-to-End Flow)

1. User inputs customer data via Streamlit UI
2. Data is sent to FastAPI backend
3. Backend:

   * Converts input into numerical format
   * Applies scaler
   * Passes data to trained model
4. Model returns prediction + probability
5. UI displays:

   * Churn / Not Churn
   * Confidence score
   * Risk level

---

## 📡 API Endpoint

**POST** `/predict`

### Request

```json id="qrjdl9"
{
  "age": 30,
  "gender": "male",
  "tenure": 10,
  "monthly_charges": 75
}
```

### Response

```json id="0p31gm"
{
  "prediction": 1,
  "label": "Churn",
  "confidence": 0.85
}
```

---

## ▶️ Run Locally

### Install dependencies

```bash id="n05lg9"
pip install -r requirements.txt
```

### Start backend

```bash id="3d5d2c"
uvicorn server:app --reload
```

### Start frontend

```bash id="mfv6c6"
streamlit run app.py
```

---

## 📊 Model Details

* Problem Type: Classification
* Target Variable: Churn (0 / 1)
* Best Model: (e.g., Random Forest / Logistic Regression)
* Features Used:

  * Age
  * Gender
  * Tenure
  * Monthly Charges

---

## 🌐 Deployment

* Backend deployed on Render
* Frontend integrated with API

---

## 📌 Future Improvements

* Add more features (contract type, payment method)
* Hyperparameter tuning (GridSearchCV)
* Improve model accuracy
* Add dashboard & analytics

---

## 👨‍💻 Author

* Your Name

---
