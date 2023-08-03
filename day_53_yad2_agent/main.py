# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import lxml
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, InvalidSessionIdException, ElementClickInterceptedException

# Function to close the ad that appears on the web page
def close_ad(driver_temp):
    time.sleep(5)
    x_button = driver_temp.find_element(By.XPATH, '/html/body/div[3]/div[3]/div/section/div/button')
    x_button.click()
    time.sleep(1)

# Function to upload apartment data to the Google Form
def upload_to_forms(google_driver, apartments_dict):
    for n, apartment in apartments_dict.items():
        address_input = google_driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input = google_driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input = google_driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input.send_keys(apartment["address"])
        price_input.send_keys(apartment["price"])
        link_input.send_keys(apartment["link"])

        # Submit the form data by simulating TAB and ENTER keys
        actions = ActionChains(driver)
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.ENTER).perform()
        time.sleep(1)
        next_button = google_driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        next_button.click()

# Start measuring the running time of the script
start = time.time()

# URLs for the source website and the target Google Form
YAD2_URL = "YOUR YAD2 URL"
GOOGLE_FORM = "YOUR GOOGLE FORM URL"

# Headers for the HTTP request
headers = {"User-Agent": "Defined",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}

# Create a webdriver for Chrome
service = Service()
driver = webdriver.Chrome(service=service)

# Navigate to the source website and perform web scraping
driver.get(YAD2_URL)
time.sleep(4)

# Get the HTML data and parse it using BeautifulSoup
html_data = driver.page_source
soup = BeautifulSoup(html_data, "lxml")

# Find all apartment containers on the page
apartment_list = soup.find_all(class_="color_container yellow")
print(len(apartment_list))
containers = driver.find_elements(By.CSS_SELECTOR, ".color_container.yellow")
print(len(containers))

# Check if the number of apartments in the containers matches the number of scraped apartments
if len(apartment_list) != len(containers):
    print("Error. Exit")
    exit(1)

# Collect links to individual apartment listings
links = []
for c in containers:
    button = c.find_element(By.CSS_SELECTOR, "button.new_tab")
    try:
        button.click()
        driver.switch_to.window(driver.window_handles[-1])
        link = driver.current_url
        links.append(link)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    except:
        close_ad(driver)
        ###############################################################
        button = c.find_element(By.CSS_SELECTOR, "button.new_tab")
        button.click()
        driver.switch_to.window(driver.window_handles[-1])
        link = driver.current_url
        links.append(link)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

# Create a dictionary to store the scraped apartment data
apartment_dict = {}
n = 0
original_window = driver.current_window_handle
for a in apartment_list:
    address = a.find("span", {"class": "title"}).get_text().strip()
    price = a.find("div", {"class": "price"}).get_text().strip()
    link = links[n]
    apartment_dict[n] = {"address": address,
                         "price": price,
                         "link": link}
    n += 1

# Navigate to the Google Form and fill it with the apartment data
driver.get(GOOGLE_FORM)
time.sleep(3)
upload_to_forms(driver, apartment_dict)

# End measuring the running time of the script
end = time.time()

# Print the running time
print(f"running time: {end-start}")

# Wait for user input before quitting the driver
input("Press Enter to continue")
driver.quit()
