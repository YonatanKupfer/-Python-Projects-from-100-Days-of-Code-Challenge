# Flight Price Alert System
This flight price alert system is a Python program that searches for low-priced flights using the Kiwi Tequila API and sends email notifications when there is a flight available at a lower price for a specific destination. The code was developed as part of the "100 Days of Code" challenge, but has been customized to suit specific needs.

## Features
* Retrieves destination data from an API and stores it in a spreadsheet.
* Updates the destination codes for each city using the FlightSearch class and the Kiwi Tequila API.
* Searches for flights from an origin city to various destinations within a specified time range.
* Sends email notifications when a low-priced flight is found for a destination.

## Prerequisites
Before running the program, ensure that you have the following prerequisites:

* Python 3.x installed on your system.
* The required Python packages installed: requests, smtplib.
* A valid Gmail account for sending email notifications.
* An API key for the Kiwi Tequila API.

## Setup and Usage
1. Clone the repository or download the code files to your local machine.
2. Install the required Python packages using pip:
```
pip install requests smtplib
```
3.Obtain an API key for the Kiwi Tequila API by following these steps:

* Visit the Kiwi Tequila API website.
* Sign up for an account or log in if you already have one.
* Go to your account settings or developer dashboard to generate an API key.
* Copy the API key.
4.  Open the main.py file and update the following variables:

* ORG_CITY_IATA: Set the IATA code of your origin city.
* MY_EMAIL: Set your Gmail email address.
* MY_PASSWORD: Set the password for your Gmail account.

5.Open the flight_search.py file and replace the TEQUILA_API_KEY variable with your own API key:
```
TEQUILA_API_KEY = "YOUR_TEQUILA_API_KEY"
```
6.  Run the main.py file to execute the flight price alert system:
```
python main.py
```
7. The program will retrieve destination data from the API, update the destination codes, and search for flights. If a low-priced flight is found for a destination, an email notification will be sent to the specified email address.

## Customization
* To add more destinations or modify the existing ones, update the destination data in the API or spreadsheet accessed by the DataManager class.
* To change the time range for flight searches, modify the tomorrow and six_months_from_today variables in the main.py file.
* To customize the email notification message, modify the body of the send_mail method in the NotificationManager class.

## Credits
The flight search functionality is implemented using the Kiwi Tequila API. Visit Kiwi Tequila API for more information.

This flight price alert system was developed as part of the "100 Days of Code" challenge, but has been customized and adapted to meet specific requirements.
