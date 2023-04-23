import requests
from datetime import timedelta, date
import smtplib
from email.mime.text import MIMEText

stocks = {
    "TSLA": "Tesla, Inc",
    "AAPL": "Apple Inc",
    "GOOG": "Alphabet Inc",
    "AMZN": "Amazon.com Inc",
}

MY_EMAIL = "testyonatan100@gmail.com"
MY_PASSWORD = "sbbztjscjvppigkf"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "WU4ZL6RPGBT94K3Q"
NEWS_API_KEY = "185abd61fc27476d929668e8dec3e04d"

# get_news function gets the news from the last day and returns a dictionary
#  with the title as key and the description
def get_news(from_date: str, symbol: str) -> dict:
    parameters = {
        "q": stocks[symbol],
        "from": from_date,
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=parameters)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]
    news_to_send = {}

    for a in news_data:
        news_to_send[a["title"]] = a["description"] + "\n" + a["url"]

    return news_to_send

# email_news function gets the arrow, the news dictionary, the difference and sends an email
#  to the email address with the news and the difference about the stock
def email_news(arrow, news, differ, symbol):

    stock_sym = symbol
    r_diff = abs(round(differ, 2))
    body = f"{stock_sym}: {arrow} {r_diff}%\n"
    for article in news:
        body = body + f"{article}.\n{news[article]}\n\n"

    msg = MIMEText(body.encode("utf-8"), 'plain', 'utf-8')
    msg["Subject"] = "Stock Alert"
    msg["From"] = MY_EMAIL
    msg["To"] = "yonatank50@gmail.com"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="ykupfer@gmail.com",
                            msg=msg.as_string()
                            )

# check_change function checks the change in the stock price and if it is more than 5% it sends an email
def check_change(symbol):
    stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
    stock_response.raise_for_status()
    data = stock_response.json()

    last_hour = data["Meta Data"]["3. Last Refreshed"]
    last_day = date.fromisoformat(last_hour.split(" ")[0])

    # get the last day that is not a weekend
    go_back = True
    prev_day = last_day
    while go_back:
        prev_day = last_day - timedelta(1)
        if prev_day.weekday() < 5:
            go_back = False

    day_before = str(prev_day) + " " + last_hour.split(" ")[1]

    last_closing_price = float(data["Time Series (60min)"][last_hour]["4. close"])
    second_day_price = float(data["Time Series (60min)"][day_before]["4. close"])
    print(last_hour)
    print(day_before)
    diff = (second_day_price - last_closing_price)/second_day_price
    print(diff)
    if abs(diff) >= 0.05:
        news_to_email = get_news(last_hour.split(" ")[0], symbol)
        up = "UP"
        if diff > 0:
            up = "DOWN"
        email_news(up, news_to_email, diff, symbol)

# main function
for stock in stocks:
    stock_parameters = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": stock,
        "interval": "60min",
        "apikey": STOCK_API_KEY
    }
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "q": stocks[stock],
        "from": "",
        "sortBy": "popularity",

    }
    check_change(stock)
