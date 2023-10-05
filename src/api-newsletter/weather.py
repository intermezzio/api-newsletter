from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_WEATHER_URL = "https://api.weatherapi.com"


def get_weather(zip_code: str = "07728"):
    url = API_WEATHER_URL + "/v1/forecast.json"
    response = requests.get(
        url, params={"q": zip_code, "days": 1, "key": os.environ["WEATHER_API_KEY"]}
    )
    response_json = response.json()
    hour_data = []

    for hour_entry in response_json["forecast"]["forecastday"][0]["hour"]:
        hour_data.append(
            {
                "hour": hour_entry["time"][-5:],
                "condition": hour_entry["condition"]["text"],
                "icon": hour_entry["condition"]["icon"],
                "temp": hour_entry["temp_f"],
            }
        )

    return hour_data
