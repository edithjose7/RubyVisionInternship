from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pdb 

# Set up the WebDriver (assuming you are using Chrome)
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.instagram.com/accounts/login/")



# Wait for the username field to be present and fill it
username_field = WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
username_field.send_keys("screechh._")



# Wait for the password field to be present and fill it
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("Edithmiriam8")



# Wait for the login button to be clickable and click it
login_button = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div"))
)
login_button.click()


not_now_button = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div"))
)
not_now_button.click()

Not_Now_button = WebDriverWait(driver,60).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"))
)
Not_Now_button.click()

# Optional: Wait to see the result (adjust the time if needed)
WebDriverWait(driver, 60).until(EC.url_changes("https://www.instagram.com/accounts/login/"))

time.sleep(100)

# Close the browser
driver.close()


