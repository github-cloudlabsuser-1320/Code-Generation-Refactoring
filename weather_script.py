import requests

def get_weather(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {condition.capitalize()}")
    else:
        print(f"Failed to get weather data for {city}. Error: {response.status_code}")

def main():
    api_key = input("Enter your OpenWeatherMap API key: ")
    while True:
        city = input("Enter city name (or 'q' to quit): ")
        if city.lower() == 'q':
            break
        get_weather(api_key, city)

if __name__ == "__main__":
    main()
