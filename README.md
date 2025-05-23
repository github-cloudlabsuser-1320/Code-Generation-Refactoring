# Code-Generation-Refactoring

# Weather App

This is a simple command-line weather application that fetches current weather data for any city using the OpenWeatherMap API.

## Requirements
- Python 3.x
- `requests` library (install with `pip install requests`)
- An OpenWeatherMap API key (get one for free at https://openweathermap.org/api)

## How to Run

1. Open a terminal and navigate to the project directory.
2. Install the required library:
   
   ```powershell
   pip install requests
   ```

3. Run the weather script:
   
   ```powershell
   python weather_script.py
   ```

4. When prompted, enter your OpenWeatherMap API key.
5. Enter the name of a city to get the current weather information (temperature, humidity, and conditions).
6. To exit, type `q` when asked for a city name.

## Example
```
Enter your OpenWeatherMap API key: YOUR_API_KEY
Enter city name (or 'q' to quit): London
Weather in London:
Temperature: 15°C
Humidity: 60%
Condition: Clear sky
Enter city name (or 'q' to quit): q
```
