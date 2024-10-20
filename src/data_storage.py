import sqlite3
import datetime
import os

# Ensure db directory exists
if not os.path.exists('db'):
    os.makedirs('db')

# Function to create the table
def create_table():
    with sqlite3.connect('db/weather.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS weather_summary')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weather_summary (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT,
                weather TEXT,
                temp REAL,
                feels_like REAL,
                date TEXT
            )
        ''')
        conn.commit()

# Function to insert weather summary
def insert_weather_summary(city, temp, feels_like, weather):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    with sqlite3.connect('db/weather.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO weather_summary (city, weather, temp, feels_like, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (city, weather, temp, feels_like, date))
        conn.commit()

# Ensure the table is created before inserting data
create_table()
