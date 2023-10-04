from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_NINJA_HEADERS = {"X-Api-Key": os.environ['API_NINJAS_KEY']}
API_NINJA_URL = "https://api.api-ninjas.com"

def get_fun_fact(num: int = 1) -> list[str]:
    url = API_NINJA_URL + "/v1/facts"
    response = requests.get(url, params={"limit": num}, headers=API_NINJA_HEADERS)
    response_json = response.json()
    return [entry["fact"] for entry in response_json]

def get_exchange_rate(pair: str) -> float:
    url = API_NINJA_URL + "/v1/exchangerate"
    response = requests.get(url, params={"pair": pair}, headers=API_NINJA_HEADERS)
    response_json = response.json()
    return response_json["exchange_rate"]
