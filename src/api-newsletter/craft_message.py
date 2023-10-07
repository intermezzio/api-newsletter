from dotenv import load_dotenv
import os

from chuck import get_joke
from newsapi import get_top_headlines
from api_ninjas import get_fun_fact, get_exchange_rate
from send_mail import send_mail
from weather import get_weather

load_dotenv()


def add_headlines() -> str:
    top_headlines = get_top_headlines(num=3)

    html_str = "<h2>Top Headlines</h2>"

    for headline in top_headlines:
        html_str += f"""<h3>{headline["title"]}</h3>
        <p>{headline["description"]}</p>
        <i>Source: <a href="{headline["url"]}">{headline["source"]["name"]}</a></i><br /><br />"""

    return html_str


def add_fun_fact() -> str:
    fun_fact = get_fun_fact()[0]
    return f"<h2>Fun Fact</h2>{fun_fact}<br /><br />"


def add_weather(zip_code: str = "07728"):
    hour_data = get_weather(zip_code)

    html_str = "<h2>Today's Forecast</h2><table><tr>"

    for hour in hour_data:
        html_str += f"""<td><b>{hour["hour"]}</b><br />
        <img src="https:{hour["icon"]}"><br />
        <p>{hour["condition"]}</p><br />
        <b>{hour["temp"]}°F</b></td>"""

    html_str += "</tr></table>"

    return html_str


def add_joke():
    joke = get_joke()

    return f"<h2>Chuck Norris Update</h2><p>{joke}</p>"


def add_exchange_rate() -> str:
    usd_eur = get_exchange_rate("USD_EUR")
    usd_gbp = get_exchange_rate("USD_GBP")
    usd_inr = get_exchange_rate("USD_INR")
    usd_jpy = get_exchange_rate("USD_JPY")
    usd_btc = get_exchange_rate("USD_BTC")

    return f"""<h2>Exchange Rates:</h2><br />
    $1 USD = <br />
    €{usd_eur} EUR<br />
    £{usd_gbp} GBP<br />
    ₹{usd_inr} INR<br />
    ¥{usd_jpy} JPY<br />
    ₿{usd_btc} BTC<br /><br />"""


if __name__ == "__main__":
    html_str = (
        add_weather()
        + add_joke()
        + add_exchange_rate()
        + add_headlines()
        + add_fun_fact()
    )
    send_mail(os.environ["RECIPIENTS"], body=html_str)  # ,adil.rasiyani@gmail.com
