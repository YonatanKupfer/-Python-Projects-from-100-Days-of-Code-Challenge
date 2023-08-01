import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Define constants for LinkedIn job search URL, user login credentials, and phone number.
LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3656983339&f_AL=true&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&refresh=true"
EMAIL = YOUR_EMAIL
PASSWORD = YOUR_PASSWORD
PHONE = YOUR_PHONE_NUMBER

# Initialize the Chrome web driver.
service = Service()
driver = webdriver.Chrome(service=service)

# Open the LinkedIn job search URL.
driver.get(LINKEDIN_URL)

# Find the "Sign in" link, click it, and fill in the login credentials.
sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in.click()
time.sleep(0.1)
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys(EMAIL)
password.send_keys(PASSWORD)

# Click the sign-in button.
sign_in_2 = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_2.click()

# Wait for the page to load after signing in.
time.sleep(5)

# Find all job cards on the page.
all_jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
print(len(all_jobs))

# Loop through each job and apply if possible.
for job in all_jobs:
    job.click()
    time.sleep(1)
    try:
        # Find the "Apply" button for the job.
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
        apply_button.click()
        time.sleep(1)
        
        # Fill in the phone number input field if it's empty.
        phone_input = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3656983339-720017503049330542-phoneNumber-nationalNumber"]')
        if phone_input.text == "":
            phone_input.send_keys(PHONE)

        # Check if the application process is complex (e.g., includes additional questions).
        # If it is, close the application and continue to the next job card.
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME ,"artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME ,"artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            # Submit the application by clicking the "Submit" button.
            submit_button.click()

        time.sleep(1)
        # Close the application confirmation modal.
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        # If there is no "Apply" button, skip this job and continue to the next one.
        print("no application button. skipped")
        continue

# Wait for user input before closing the browser window.
input("Press Enter to close the browser window.")
driver.quit()
