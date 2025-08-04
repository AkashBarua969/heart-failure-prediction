# db.py
import sqlite3

def init_db():
    conn = sqlite3.connect("predictions.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            sex TEXT,
            chest_pain TEXT,
            resting_bp INTEGER,
            cholesterol INTEGER,
            fbs INTEGER,
            ecg TEXT,
            max_hr INTEGER,
            angina TEXT,
            oldpeak REAL,
            slope TEXT,
            result TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()
