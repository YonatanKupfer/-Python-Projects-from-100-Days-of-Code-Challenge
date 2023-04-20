# ISS Tracker
This is a Python script written as part of the "100 Days of Code" course that uses APIs to track the International Space Station (ISS) and sends an email notification when it is passing over the user's location during nighttime.

## Prerequisites
To run this script, you need to have Python 3 installed on your machine. You also need to install the requests and smtplib libraries using pip:

pip install requests smtplib

## Usage
To use this script, you need to provide your email address and password as well as your location's latitude and longitude in the script's constants at the beginning of the code:

MY_EMAIL = "your_email_address@gmail.com"
MY_PASSWORD = "your_email_password"
MY_LAT = 51.509865 # your latitude
MY_LNG = -0.118092 # your longitude

Then, run the script using the following command:

python iss_tracker.py

The script will start tracking the ISS and sending email notifications when it is passing over your location during nighttime.

## How it works
The script uses two APIs to track the ISS and determine if it is passing over the user's location during nighttime:

1. Open Notify API: This API provides information about the ISS's current location. The script makes a request to the API and extracts the latitude and longitude of the ISS.

2. Sunrise Sunset API: This API provides information about the sunrise and sunset times for a given location. The script makes a request to the API and extracts the sunrise and sunset times for the user's location.

The script then compares the ISS's latitude and longitude with the user's location and checks if it is within a 5-degree range. If it is, the script compares the current time with the sunset and sunrise times and checks if it is nighttime. If it is, the script sends an email notification to the user's email address using the Gmail SMTP server.

The script runs in an infinite loop and checks the ISS's location and the current time every minute using the time.sleep(60) function.

## Security considerations
Note that the script stores the user's email address and password in plain text, which is not recommended for security reasons. To avoid this, you can use environment variables or a configuration file to store sensitive information.

## Acknowledgments
This script was written as part of the "100 Days of Code" course by Dr. Angela Yu.
