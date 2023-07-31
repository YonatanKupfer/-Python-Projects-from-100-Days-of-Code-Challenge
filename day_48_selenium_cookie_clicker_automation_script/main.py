import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Create a new Chrome service and WebDriver
service = Service()
driver = webdriver.Chrome(service=service)

# Navigate the browser to the "Cookie Clicker" game page
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Find the cookie element on the page and store it in the 'cookie' variable
cookie = driver.find_element(By.ID, "cookie")

# Calculate the end time of the game (5 minutes from the current time) and the time for the next action (5 seconds from the current time)
game_time = time.time() + 60 * 5
five_sec = time.time() + 5

# Main loop that runs until the current time exceeds the game time
while True:
    # Check if it's time for the next action
    if time.time() > game_time:
        break

    if time.time() > five_sec:
        try:
            # Read the amount of money available and the prices of various upgrades
            money = float(driver.find_element(By.ID, "money").text.replace(",", ""))
            portal = float(driver.find_element(By.CSS_SELECTOR, "#buyPortal b").text.split(" ")[2].replace(",", ""))
            shipment = float(driver.find_element(By.CSS_SELECTOR, "#buyShipment b").text.split(" ")[2].replace(",", ""))
            mine = float(driver.find_element(By.CSS_SELECTOR, "#buyMine b").text.split(" ")[2].replace(",", ""))
            factory = float(driver.find_element(By.CSS_SELECTOR, "#buyFactory b").text.split(" ")[2].replace(",", ""))
            grandma = float(driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").text.split(" ")[2].replace(",", ""))
            cursor = float(driver.find_element(By.CSS_SELECTOR, "#buyCursor b").text.split(" ")[2].replace(",", ""))

            # Attempt to buy upgrades in a certain order based on available money
            if money >= portal:
                driver.find_element(By.ID, "buyPortal").click()
                money -= portal
            if money >= shipment:
                driver.find_element(By.ID, "buyShipment").click()
                money -= shipment
            if money >= mine:
                driver.find_element(By.ID, "buyMine").click()
                money -= mine
            if money >= factory:
                driver.find_element(By.ID, "buyFactory").click()
                money -= factory
            if money >= grandma:
                driver.find_element(By.ID, "buyGrandma").click()
                money -= grandma
            if money >= cursor:
                driver.find_element(By.ID, "buyCursor").click()
                money -= cursor
        except:
            # If an exception occurs during the upgrade purchase, print "missed"
            print("missed")

        # Reset the timer for the next action to 5 seconds from the current time
        five_sec = time.time() + 5

    try:
        # Click on the cookie element to earn money
        cookie.click()
    except:
        # If an exception occurs while clicking the cookie, print "missed cookie"
        print("missed cookie")

# The loop ends after 5 minutes. Try to find and print the cookies per second (CPS) value from the page.
cps = driver.find_element(By.ID, "cps").text.split(" ")[2]
print(cps)

# Wait for user input (pressing Enter) before closing the browser window and quitting the WebDriver.
input("Press Enter to close the browser window.")
driver.quit()
