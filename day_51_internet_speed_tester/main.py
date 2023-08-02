import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Create a new Service object for the Chrome web driver
service = Service()

# The URL of the speed test website
SPEEDTEST_URL = "https://www.speedtest.net/"


class InternetSpeedTester:
    def __init__(self, service):
        # Initialize the Chrome web driver using the provided service object
        self.driver = webdriver.Chrome(service=service)
        self.up = 0  # Initialize the upload speed variable to 0
        self.down = 0  # Initialize the download speed variable to 0

    def get_internet_speed(self):
        # Open the speed test website using the Chrome web driver
        self.driver.get(SPEEDTEST_URL)

        # Wait for 10 seconds to ensure the page is fully loaded
        time.sleep(10)

        # Locate and click the "Go" button to start the speed test
        go = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go.click()

        # Wait for 80 seconds to allow the speed test to complete
        time.sleep(80)

        # Extract the download and upload speeds from the page and store them as floating-point numbers
        self.down = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)

    def print_internet_speed(self):
        # Print the internet speed test results on the console
        print("Your internet speed test results are:")
        print(f"Download speed: {self.down} Mbps.")
        print(f"Upload speed: {self.up} Mbps.")


# Create an instance of the InternetSpeedTester class with the provided service object
tester = InternetSpeedTester(service=service)

# Perform the internet speed test
tester.get_internet_speed()

# Print the test results on the console
tester.print_internet_speed()
