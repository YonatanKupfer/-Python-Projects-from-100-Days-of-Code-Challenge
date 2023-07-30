# Price Tracker - 100 Days of Code Challenge

This project is a price tracker script developed as part of the "100 Days of Code" challenge. It allows you to monitor the price of a product on AliExpress and receive email notifications when the price drops below a certain threshold.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Dependencies](#dependencies)
5. [How It Works](#how-it-works)
6. [Important Notes](#important-notes)
7. [Credits](#Credits)

## Introduction
The Price Tracker is a Python script that uses web scraping to retrieve the price of a specific product from the AliExpress website. It then compares the price with a predefined threshold and sends an email notification to the user if the price drops below this threshold. This tool can be handy for those who want to keep track of price changes and take advantage of discounts on AliExpress.

## Installation
1. Ensure you have Python installed on your machine (Python 3.6 or higher is recommended).
2. Clone or download this repository to your local machine.

## Usage
1. Open the `main.py` script in a text editor or Python IDE of your choice.
2. Set the `URL` variable to the product page URL from AliExpress that you want to track.
3. Define the `BUY_PRICE` variable to the price threshold you want to receive an email notification for.
4. Modify the `MY_EMAIL` and `MY_PASSWORD` variables to use your own Gmail email and password (or app password) for sending the email notification.
5. Run the script using the command `python price_tracker.py`.
6. The script will check the price of the product, and if it's below the specified threshold, it will send an email to your specified recipient.

## Dependencies
The following libraries are required to run the Price Tracker:
- requests
- BeautifulSoup from bs4
- lxml
- smtplib
- email.mime.text from email

You can install these dependencies using `pip` with the following command:
```
pip install requests beautifulsoup4 lxml
```

## How It Works
1. The script sends an HTTP GET request to the provided AliExpress product URL using the `requests` library.
2. The HTML content of the page is parsed using BeautifulSoup with the `lxml` parser to extract relevant data, including the product price.
3. The script compares the extracted price with the specified threshold (BUY_PRICE).
4. If the price is below the threshold, it sends an email notification to the specified recipient (configured using the `MY_EMAIL` and `MY_PASSWORD` variables) using the Gmail SMTP server.

## Important Notes
- This script scrapes data from AliExpress, and web scraping may be subject to terms of service or usage restrictions. Use this script responsibly and respect the website's policies.
- Be cautious about providing your Gmail password directly in the script. Consider using an app password or a dedicated email account for this purpose.
- Sending a large number of automated emails may trigger Gmail's security measures.

## Credits
This product price alert system was developed as part of the "100 Days of Code" challenge, but has been customized and adapted to meet specific requirements.
