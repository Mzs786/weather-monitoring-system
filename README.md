# Weather Monitoring System

This is a Python-based weather monitoring system that fetches weather data from the OpenWeatherMap API and stores it in an SQLite database. The system allows you to retrieve real-time weather information for multiple cities and store the data for future analysis.

## Features

- Fetches weather data for multiple cities from the OpenWeatherMap API.
- Stores weather data (city, weather description, temperature, feels-like temperature) in an SQLite database.
- Scheduled to fetch and store weather data at regular intervals using the `APScheduler`.
- Simple and lightweight, using SQLite for local data storage.

## Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.9+**
- **SQLite3** (comes pre-installed with Python)

## Installation and Setup

``1. Clone the repository``

First, clone the repository to your local machine:

```
git clone https://github.com/your-username/weather-monitoring-system.git
```
Change the directory:
```
cd weather-monitoring-system
```

``2. Set up a virtual environment (optional but recommended)``
It’s a good practice to use a virtual environment to manage dependencies.

# For Windows
```
python -m venv venv
venv\Scripts\activate
```

# For macOS/Linux
```
python3 -m venv venv
source venv/bin/activate
```

``3. Install the required Python packages``

Install the dependencies listed in the requirements.txt file:
```
pip install -r requirements.txt
```

``4. Obtain an API Key from OpenWeatherMap``

You need an API key to fetch weather data from the OpenWeatherMap API. Follow these steps:

Sign up at OpenWeatherMap.

Go to the API Keys section in your account.

Copy your API key.


``5. Add your API Key to the application``

In the src/weather_data_fetcher.py file, replace the placeholder API key with your actual API key:
```
api_key = "your_openweather_api_key_here"
```

``6. Run the application``

Now that everything is set up, you can run the application:
```
python main.py
```
The application will start fetching weather data for the configured cities and store it in an SQLite database called weather_data.db.

How the Application Works

``Fetching Weather Data:``

The get_weather_data_for_cities function in src/weather_data_fetcher.py retrieves weather data from the OpenWeatherMap API for a list of cities.


``Storing Data in SQLite:``

The store_weather_data function in src/data_storage.py stores the fetched weather data into an SQLite database (weather_data.db).

``Scheduler:``

The APScheduler library is used to schedule weather data fetching at regular intervals (e.g., every 10 seconds or 5 minutes). 
You can adjust the scheduling interval in the src/scheduler.py file.

``Directory Structure``
```
weather-monitoring-system/
│
├── src/
│   ├── data_storage.py          # Handles storing data into SQLite
│   ├── scheduler.py             # Manages scheduling of the data fetching
│   ├── weather_data_fetcher.py   # Fetches weather data from OpenWeatherMap API
│
├── main.py                      # Entry point of the application
├── weather_data.db              # SQLite database (created after the app runs)
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation (this file)
```

``Customization:``

Adding/Removing Cities: You can modify the list of cities for which you want to fetch weather data in the src/weather_data_fetcher.py file.

```
cities = ["Delhi", "Mumbai", "Chennai", "Bengaluru", "Kolkata"]
```


``Scheduling Interval:`` To change how frequently the weather data is fetched, edit the interval in the src/scheduler.py file:


```
scheduler.add_job(fetch_weather_and_store_data, 'interval', minutes=5)
```
# Fetch every 5 minutes


``Troubleshooting:``

Error: "Table has no column named X": This error indicates that your SQLite table schema doesn't match the data you're trying to insert. Check that your weather_summary table schema in data_storage.py matches the data structure.

Request Errors: If you encounter issues fetching data from the API, check your API key and make sure you're not exceeding the API rate limit.


``License``

This project is licensed under the MIT License. See the LICENSE file for details.


