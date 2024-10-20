import sys
import os
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from weather_data_fetcher import get_weather_data_for_cities, calculate_daily_summary
from data_storage import insert_weather_summary, create_table

# Ensure the root directory is in the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Initialize the scheduler
scheduler = BackgroundScheduler()
logging.basicConfig(level=logging.INFO)

cities = ["Delhi", "Mumbai", "Chennai", "Bengaluru", "Kolkata", "Hyderabad"]
api_key = 'your_openweather_api_key_here'
user_thresholds = {
    'temperature': 35,
    'condition': 'Rain'
}

# Create table before inserting data
create_table()

def fetch_weather_and_store_data():
    try:
        weather_data = get_weather_data_for_cities(cities, api_key)
        for city_weather in weather_data:
            city = city_weather['city']
            weather = city_weather['weather']
            temp = city_weather['temp']
            feels_like = city_weather['feels_like']
            # Display the weather data in lines
            logging.info(f"City: {city}\nWeather: {weather}\nTemp: {temp}°C\nFeels Like: {feels_like}°C\n")
            insert_weather_summary(city, temp, feels_like, weather)
            logging.info(f"Weather data for {city} inserted successfully!")
            # Check for alerts
            if temp > user_thresholds['temperature'] or weather == user_thresholds['condition']:
                logging.warning(f"Alert: {city} has reached threshold conditions!")
        
        # Calculate and print daily summaries
        daily_summary = calculate_daily_summary(weather_data)
        logging.info(f"Daily Summary:\n{daily_summary}")
        
    except Exception as e:
        logging.error(f"An error occurred during weather data processing: {e}")

def run_scheduler():
    try:
        scheduler.add_job(fetch_weather_and_store_data, 'interval', minutes=5)
        scheduler.start()
        while True:
            pass
    except Exception as e:
        logging.error(f"An error occurred during scheduler execution: {e}")
        scheduler.shutdown()
