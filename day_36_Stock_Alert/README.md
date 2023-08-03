# Stock Alert Application
This is a Python application that sends an email alert when the stock price of certain companies changes more than 5% since the last closing price. The application uses the Alpha Vantage API to get real-time stock prices and the News API to get the latest news about the companies. It sends an email with the news and the difference about the stock to a specific email address.

I created this application as part of my own learning process and as a personal project. It may not be suitable for production use without further modifications.

## Installation
1. Copy the code and save it in a new file at your desired location.

2. Install the required packages using pip:

```pip install -r requirements.txt```

3. Create an account and get API keys for both Alpha Vantage and News API.

4. Create a Gmail account for the app to send emails.

5. Open the main.py file and update the stocks dictionary with the symbols and names of the companies you want to track.

6. Update the MY_EMAIL and MY_PASSWORD variables with the Gmail account credentials.

7. Update the NEWS_API_KEY and STOCK_API_KEY variables with the API keys you obtained.

## Usage
To run the application, simply run the main.py file using Python:

```python main.py```

The application will check the stock prices and send an email if there has been a change of more than 5% since the last closing price.

## Acknowledgements
This project was inspired by the "100 Days of Code" challenge, but I made it my own by adding my own features and functionality.

The following APIs were used in this project:

* Alpha Vantage
* News API
