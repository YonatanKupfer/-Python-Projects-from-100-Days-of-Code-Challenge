import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
from email.mime.text import MIMEText



URL = YOUR ITEM'S URL
BUY_PRICE = YOUR BUY PRICE
MY_EMAIL = YOUR EMAIL
MY_PASSWORD = YOUR PASSWORD

headers = {"User-Agent": "Defined",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

r = requests.get(URL, headers=headers)
r.raise_for_status()
page = r.text
print(page)

soup = BeautifulSoup(page, "lxml")
price_tag = soup.find(name="meta", property="og:title")
price = float(price_tag['content'].split("₪")[0].strip())

if price < BUY_PRICE:
    body = f"The item you wanted is now {price} at: {URL}"
    msg = MIMEText(body.encode("utf-8"), 'plain', 'utf-8')
    msg["Subject"] = "Item Price Alert"
    msg["From"] = MY_EMAIL
    msg["To"] = MY_EMAIL

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=msg.as_string()
                            )

