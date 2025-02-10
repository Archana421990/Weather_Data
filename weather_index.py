import requests
def get_weather(city):
    api_key = "your_api_key" # Replace with your actual API key
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(BASE_URL)
    return response.json()
def display_weather(data):
    if data["cod"] == 200:
        city = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")
    else:
        print("City not found. Please check the name and try again.")

city = input("Enter city name: ")
weather_data = get_weather(city)
display_weather(weather_data)

