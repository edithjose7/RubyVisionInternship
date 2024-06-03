
import logging  # Import the logging module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Start the WebDriver
driver = webdriver.Chrome()
logging.info("Opening the login page")
driver.get("https://128.199.177.68:30443/login")
logging.info("Waiting for the username field to be present")
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login"))
)
logging.info("Entering username")
username_field.send_keys(" ")
logging.info("Finding the password field")
password_field = driver.find_element(By.ID, "password")
logging.info("Entering password")
password_field.send_keys(" ")
logging.info("Waiting for the login button to be clickable")
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[3]/a[1]"))
)
logging.info("Clicking the login button")
login_button.click()
logging.info("Waiting for the URL to change to the products page")
WebDriverWait(driver, 10).until(EC.url_changes("https://128.199.177.68:30443/products"))
logging.info("Login successful and navigated to products page")
time.sleep(60)
# Always make sure to close the driver
driver.quit()
logging.info("Closed the WebDriver")








