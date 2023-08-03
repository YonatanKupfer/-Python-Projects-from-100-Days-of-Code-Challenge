# Yad2 Web Scraper & Google Form Uploader

This Python script allows you to scrape apartment data from Yad2 (a popular Israeli real estate website) and automatically upload it to your custom Google Form. It is intended to be used for personal use and educational purposes. Please be mindful of the website's terms of service and the ethical implications of web scraping.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Disclaimer](#disclaimer)

## Description

This project was developed as part of the "100 Days of Code" challenge, where I aimed to automate the process of searching for apartments on Yad2 and organizing the data in a Google Form. The script is designed to speed up the process of apartment hunting and assist in data management.

## Features

- Scrapes apartment data from Yad2 based on user-defined preferences.
- Automatically fills a custom Google Form with the scraped data for easy organization and analysis.

## Requirements

To run the script, you need the following:

- Python 3.x
- Chrome WebDriver
- Selenium
- BeautifulSoup
- lxml

## Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/yourusername/yad2-scraper.git
```

2. Install the required Python libraries using pip:

```
pip install selenium
pip install beautifulsoup4
pip install lxml
```

3. Download the Chrome WebDriver and add it to your system's PATH. You can download it from the official website: https://sites.google.com/a/chromium.org/chromedriver/downloads

## Usage

Before running the script, you need to configure it with your preferences. Follow these steps:

1. Go to the Yad2 website (https://www.yad2.co.il/) and apply the desired filters (e.g., area, price range, number of rooms, etc.) to narrow down your apartment search.
2. Copy the URL of the search results page with your preferences.
3. Create a Google Form where you want to store the scraped data. Copy the URL of the Google Form.

Now you are ready to run the script:

```
python main.py
```

The script will navigate to the Yad2 search results page, scrape the apartment data, open each apartment listing to retrieve detailed information, and then upload the data to your custom Google Form.

## Disclaimer

This script is intended for personal use and educational purposes only. Using web scraping to interact with websites may violate their terms of service. Please review the terms of service of both Yad2 and Google Forms before using this script.

The developer of this script is not responsible for any misuse or legal issues arising from its usage.
