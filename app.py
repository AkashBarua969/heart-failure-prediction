from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import sqlite3
from db import init_db
from datetime import datetime, timedelta

app = Flask(__name__)

# Load AdaBoost model
model = pickle.load(open("ada_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        features = [
            data["Age"],
            1 if data["Sex"] == "M" else 0,
            {"ATA": 0, "NAP": 1, "ASY": 2, "TA": 3}[data["ChestPainType"]],
            data["RestingBP"],
            data["Cholesterol"],
            data["FastingBS"],
            {"Normal": 0, "ST": 1, "LVH": 2}[data["RestingECG"]],
            data["MaxHR"],
            1 if data["ExerciseAngina"] == "Y" else 0,
            data["Oldpeak"],
            {"Up": 0, "Flat": 1, "Down": 2}[data["ST_Slope"]]
        ]

        input_data = np.array([features])
        prediction = model.predict(input_data)[0]

        # Format Bangladesh time
        bd_time = datetime.utcnow() + timedelta(hours=6)
        formatted_time = bd_time.strftime("%Y-%m-%d %H:%M:%S")

        # Save to database with timestamp
        conn = sqlite3.connect("predictions.db")
        c = conn.cursor()
        c.execute("""
            INSERT INTO predictions 
            (age, sex, chest_pain, resting_bp, cholesterol, fbs, ecg, max_hr, angina, oldpeak, slope, result, timestamp)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data["Age"],
            data["Sex"],
            data["ChestPainType"],
            data["RestingBP"],
            data["Cholesterol"],
            data["FastingBS"],
            data["RestingECG"],
            data["MaxHR"],
            data["ExerciseAngina"],
            data["Oldpeak"],
            data["ST_Slope"],
            "Heart Disease" if prediction == 1 else "Healthy",
            formatted_time
        ))
        conn.commit()
        conn.close()

        return jsonify({"prediction": int(prediction)})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/history")
def history():
    conn = sqlite3.connect("predictions.db")
    c = conn.cursor()
    c.execute("SELECT * FROM predictions ORDER BY timestamp DESC")
    records = c.fetchall()
    conn.close()
    return render_template("history.html", records=records)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
