import requests
import tkinter as tk
from tkinter import messagebox

# OpenWeatherMap API Key
API_KEY = "7a8d01a5b65efd47d45a9e9b28cef7b2"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

#BASE_URL="https://api.openweathermap.org/data/2.5/weather?q={city}&appid={7a8d01a5b65efd47d45a9e9b28cef7b2}"
#BASE_URL="https://api.openweathermap.org/data/2.5/weather?q=Mumbai&appid=7a8d01a5b65efd47d45a9e9b28cef7b2"
#BASE_URL="https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={7a8d01a5b65efd47d45a9e9b28cef7b2}"
#BASE_URL="https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={0ef9fdabd5826a30932cf41048fd6553}"

#BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
 
    params = {
        "q": f"{city},IN",  # Adding country code
        "appid": API_KEY,
        "units": "metric"
    }

    
    """ params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    } """

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_info = f"""
        City: {data['name']}
        Temperature: {data['main']['temp']}°C
        Weather: {data['weather'][0]['description'].title()}
        Humidity: {data['main']['humidity']}%
        Wind Speed: {data['wind']['speed']} m/s
        """
        weather_label.config(text=weather_info)
    else:
        messagebox.showerror("Error", "City not found or API error.")

# Create GUI Window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

# UI Elements
tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

fetch_button = tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather)
fetch_button.pack(pady=10)

weather_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
weather_label.pack(pady=10)

# Run the App
root.mainloop()
