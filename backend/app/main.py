from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
from datetime import datetime

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5175"],  # React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "cc6a212379de921ea872d11dce038644"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Request body model
class WeatherRequest(BaseModel):
    city: str

# Helper function: Get greeting based on time of day
def get_greeting():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"

@app.post("/weather")
async def get_weather(request: WeatherRequest):
    city = request.city
    try:
        # Request current weather data
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            weather_description = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            # Create an interactive response
            return {
                "response": (
                    f"{get_greeting()}, the weather in {data['name']} is {weather_description}.\n"
                    f"The temperature is {temperature}°C with a humidity of {humidity}% "
                    f"and wind speed of {wind_speed} m/s.\n"
                    f"Let me know if you'd like to hear tomorrow's forecast!"
                )
            }
        elif response.status_code == 404:
            raise HTTPException(status_code=404, detail="City not found. Try checking for typos or specify a nearby city.")
        else:
            raise HTTPException(status_code=response.status_code, detail="Unable to fetch weather data at the moment.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.post("/forecast")
async def get_forecast(request: WeatherRequest):
    # Example for adding multi-day forecast (requires OpenWeatherMap's forecast API)
    city = request.city
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast"
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(forecast_url, params=params)

        if response.status_code == 200:
            data = response.json()
            # Get tomorrow's forecast (assuming 3-hour intervals, forecast for 24 hours ahead is at index 8)
            tomorrow_forecast = data['list'][8]
            description = tomorrow_forecast['weather'][0]['description']
            temp = tomorrow_forecast['main']['temp']

            return {
                "response": (
                    f"Tomorrow in {city}, expect {description} with a temperature of {temp}°C.\n"
                    f"Would you like to hear more about the week's forecast?"
                )
            }
        else:
            raise HTTPException(status_code=404, detail="Unable to fetch the forecast. Try a different city.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
