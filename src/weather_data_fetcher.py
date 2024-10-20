import random
import datetime
import pandas as pd
from collections import Counter
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()

def get_weather_data_for_cities(cities, api_key):
    weather_data = []
    for city in cities:
        data = get_weather(city, api_key)
        weather_data.append({
            'city': city,
            'weather': data['weather'][0]['main'],
            'temp': kelvin_to_celsius(data['main']['temp']),
            'feels_like': kelvin_to_celsius(data['main']['feels_like']),
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'date': datetime.datetime.now().strftime("%Y-%m-%d")
        })
    return weather_data

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def simulate_weather_updates(cities, num_days):
    simulated_data = []
    for _ in range(num_days):
        for city in cities:
            temp = round(random.uniform(15, 35), 2)
            feels_like = round(temp + random.uniform(-2, 2), 2)
            weather = random.choice(['Clear', 'Rain', 'Snow', 'Clouds'])
            simulated_data.append({
                'city': city,
                'temp': temp,
                'feels_like': feels_like,
                'weather': weather,
                'date': (datetime.datetime.now() + datetime.timedelta(days=_)).strftime("%Y-%m-%d")
            })
    return simulated_data

def calculate_daily_summary(weather_data):
    df = pd.DataFrame(weather_data)
    daily_summary = df.groupby(['city', 'date']).agg(
        avg_temp=('temp', 'mean'),
        max_temp=('temp', 'max'),
        min_temp=('temp', 'min'),
        dominant_condition=('weather', lambda x: Counter(x).most_common(1)[0][0])
    ).reset_index()
    return daily_summary

def get_forecast(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}"
    response = requests.get(url)
    return response.json()

def summarize_forecast(forecast_data):
    df = pd.DataFrame(forecast_data['list'])
    summary = df.groupby(df['dt_txt'].str.slice(0, 10)).agg(
        avg_temp=('main.temp', 'mean'),
        max_temp=('main.temp_max', 'max'),
        min_temp=('main.temp_min', 'min'),
        dominant_condition=('weather', lambda x: Counter([d['main'] for d in x]).most_common(1)[0][0])
    ).reset_index()
    return summary
