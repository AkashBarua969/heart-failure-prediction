# ❤️ HeartCare by Akash – Heart Failure Prediction System

A Machine Learning-based Heart Failure Prediction System built with Flask and AdaBoost. This web app predicts the risk of heart failure based on user-provided health data, offers personalized health advice, and lists top heart specialists in Bangladesh.

---

## 🧪 Dataset Used
- [Heart Failure Prediction Dataset (Kaggle)](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction)
- **Features:** Age, Sex, Chest Pain Type, Resting BP, Cholesterol, ECG, Max Heart Rate, etc.

---

## 🔧 Technologies Used
- Python 3
- Flask Web Framework
- AdaBoost (Machine Learning)
- SQLite3 (Database)
- Bootstrap 5 (Frontend)
- HTML, CSS, JavaScript

---

## 📁 Project Structure

heart-failure-prediction/
│
├── app.py # Main Flask app
├── db.py # Database schema (SQLite)
├── ada_model.pkl # Trained AdaBoost model
├── Heart Failure Prediction Dataset.csv
├── predictions.db # Prediction history (auto-generated)
│
├── templates/ # HTML pages
│ ├── index.html # Homepage with form
│ └── history.html # History table
│
├── static/
│ └── styles.css # Custom styling


---

## 🚀 How It Works
1. User fills a web form with their medical data.
2. Backend processes input using the AdaBoost ML model.
3. Model predicts the likelihood of heart disease.
4. Result is displayed as "Healthy" or "Heart Disease".
5. The system stores prediction data with a timestamp in the database.
6. Users can view past predictions and receive health guidance.

---

## 👨‍⚕️ Health Advice
If the system detects risk:
- ✅ Exercise daily (at least 30 minutes)
- 🚭 Quit smoking and limit alcohol
- 🥗 Eat more vegetables, less salt/sugar
- 😌 Reduce stress through hobbies or meditation
- 🩺 Regularly monitor blood pressure and cholesterol

---

## 🫀 Top Heart Specialists in Bangladesh
- [🔗 Prof. Dr. Munshi Md. Mojibur Rahman – Green Life Hospital](https://greenlifehospital.com.bd/consultant/professor-dr-munshi-md-mojibur-rahman)
- [🔗 Prof. Dr. Shishir Basak – Mount Adora Hospital, Sylhet](https://mountadora.com/doctors/prof-dr-shishir-basak/)
- [🔗 Prof. Dr. Dhiman Banik – National Heart Foundation](https://www.doctorbangladesh.com/dr-dhiman-banik/)

---

## 📬 Contact
**Project by:** Akash Barua  
**Department of CSE**, Sylhet International University  
📧 Email: [akashbarua969@gmail.com](mailto:akashbarua969@gmail.com)

---

> 🔒 *Note: This project is intended for academic and demonstration purposes only.*

