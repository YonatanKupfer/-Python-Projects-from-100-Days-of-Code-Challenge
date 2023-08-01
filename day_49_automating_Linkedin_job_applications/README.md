# LinkedIn Job Application Automation using Selenium

## Description

This Python script automates the job application process on LinkedIn. It uses Selenium, a web automation library, to navigate to a specific job search page on LinkedIn, log in with the provided credentials, and then apply for multiple job listings. The script fills in the phone number if required and handles complex application forms, if any.

This project was developed as part of the "100 Days of Code" challenge, but the implementation has been customized to meet specific requirements.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x: The script requires Python 3.x to run.
- Selenium: Install the Selenium library using `pip install selenium`.
- Chrome Web Driver: Download the appropriate Chrome Web Driver for your Chrome browser version from the official Selenium website (https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure to place the driver executable in a directory that is included in your system's PATH.

## Usage

1. Update Constants: Open the Python script and update the `LINKEDIN_URL`, `EMAIL`, `PASSWORD`, and `PHONE` constants at the beginning of the script with your own LinkedIn job search URL, login credentials, and preferred phone number.

2. Run the Script: Execute the script using the Python interpreter.

```
python main.py
```

3. Script Execution: The script will open a Chrome browser window, navigate to the LinkedIn job search page, sign in with the provided credentials, and start applying to relevant jobs automatically. If a phone number is required, it will be filled in with the provided number. The script handles complex application forms, if any, and prints relevant messages accordingly.

4. Confirmation: The script will wait for user input before closing the browser window. Press Enter to close the browser.

## Note

Please use this script responsibly and in compliance with LinkedIn's terms of service. Automation scripts like this may violate LinkedIn's usage policy, and improper use can lead to account suspension or other consequences.

This project was developed as part of the "100 Days of Code" challenge, and the implementation has been customized to suit the user's needs. Feel free to modify the script as per your requirements.

