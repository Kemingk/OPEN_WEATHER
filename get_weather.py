import requests
import os
from dotenv import load_dotenv
import re

# Load your API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    """
    Fetch weather for the given city and print it nicely.
    """
    # 1. Create the API endpoint URL
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # 2. Set query parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # temperature in Celsius
    }
    
    # 3. Make the request
    response = requests.get(url, params=params)
    
    # 4. Parse JSON
    data = response.json()
    
    # 5. Extract key info
    city_name = data["name"]
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    
    # 6. Print
    output = f"""
        This is a Weather Report for {city} 🌎
        -----------------------------
        🌡️  Temperature: {temp} °C
        💧  Humidity:    {humidity} %
        ☁️  Description: {description.capitalize()}
        """
    output = re.sub(r"\s+\n", "\n", output)  
    print(output)
    print(f"In {city_name}, temperature is {temp}°C with {description} and the humidity is {humidity}%.")

# Try it
city = input("Enter a US city: ")
get_weather(city)
