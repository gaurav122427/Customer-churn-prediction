# Customer Churn Prediction

A machine learning project that predicts whether a customer is likely to churn (leave the service) based on customer behavior and usage patterns.  
The project includes data preprocessing, model training, and deployment using a simple web interface.

---

## 📌 Project Overview
Customer churn is a major challenge for subscription-based businesses.  
This project helps identify customers who are at risk of churning so that businesses can take proactive retention actions.

---

## 🚀 Features
- Data preprocessing and feature selection
- Machine learning model training
- Churn prediction (Yes / No)
- Interactive web application
- Easy-to-use interface for non-technical users

---

## 🛠️ Tech Stack
- **Python**
- **Pandas, NumPy**
- **Scikit-learn**
- **Streamlit** (for deployment)
- **Pickle** (model serialization)

---

## 📂 Project Structure
Customer-churn-prediction/ │ ├── customer-churn.ipynb   # Jupyter notebook for data analysis & model training ├── model.pkl              # Trained machine learning model ├── app.py                 # Streamlit web application ├── requirements.txt       # Required Python libraries ├── README.md              # Project documentation └── LICENSE
---

## 📊 Machine Learning Model
- Algorithm used: Logistic Regression / Random Forest (based on implementation)
- Input features:
  - Tenure
  - Monthly Charges
  - Total Charges
- Output:
  - **Churn = Yes / No**

---

## 🌐 Live Demo
🔗 **Live Application:**  
[link](https://customer-churn-prediction.streamlit.app/)
Example:

---

## ▶️ How to Run Locally
1. Clone the repository:
```bash
git clone https://github.com/gaurav122427/Customer-churn-prediction.git
