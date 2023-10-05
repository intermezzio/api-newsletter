import requests

CHUCK_API_URL = "https://api.chucknorris.io"


def get_joke() -> str:
    url = CHUCK_API_URL + "/jokes/random"
    params = {
        "category": "animal,career,dev,fashion,food,history,money,movie,music,science,sport,travel"
    }
    response = requests.get(url, params=params)
    response_json = response.json()
    return response_json["value"]
