import requests
from datetime import datetime as dt
import smtplib
import time

MY_EMAIL = "testyonatan100@gmail.com"
MY_PASSWORD = "sbbztjscjvppigkf"


MY_LAT = 32.110569
MY_LNG = 35.036121

# function to check if the ISS is above you right now
def is_above():
    response2 = requests.get(url="http://api.open-notify.org/iss-now.json")
    response2.raise_for_status()

    data2 = response2.json()

    longitude = float(data2["iss_position"]["longitude"])
    latitude = float(data2["iss_position"]["latitude"])

    iss_position = (longitude, latitude)
    if MY_LNG + 5 >= longitude >= MY_LNG - 5 and MY_LAT + 5 >= latitude >= MY_LAT - 5:
        return True
    return False

# function to check if it is currently dark
def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,

    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_h = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_h = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print(sunrise_h)
    print(sunset_h)
    time_now = dt.now()
    print(time_now.hour)
    if time_now.hour > sunset_h or time_now.hour < sunrise_h:
        return True
    return False

# If the ISS is close to my current position and it is currently dark 
# Then send me an email to tell me to look up.
while True:
    time.sleep(60)
    if is_above() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="yonatank50@gmail.com",
                                msg="Subject:ISS is above you\n\nLook up!"
                                )



