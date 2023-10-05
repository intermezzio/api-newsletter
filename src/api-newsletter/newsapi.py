from dotenv import load_dotenv
import os
import requests

load_dotenv()

NEWSAPI_HEADERS = {"X-Api-Key": os.environ["NEWSAPI_KEY"]}
NEWSAPI_URL = "https://newsapi.org"


def get_top_headlines(num: int | None = None):
    url = NEWSAPI_URL + "/v2/top-headlines"
    params = {
        "sources": "abc-news,bbc-news,associated-press,al-jazeera-english,bloomberg,business-insider,cbs-news,cnn,espn,fortune,msnbc,nbc-news,politico,reuters,the-huffington-post,the-wall-street-journal,the-washington-post,time,usa-today",
    }
    response = requests.get(url, params=params, headers=NEWSAPI_HEADERS)
    response_json = response.json()

    if num is None:
        return response_json["articles"]
    else:
        return response_json["articles"][:num]
