from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Create a new instance of the Firefox driver
driver = webdriver.Chrome(options=options)

# Create maximize windows display
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Navigate to a website
driver.get('https://secondhand.binaracademy.org/users/sign_in')

try:
    # Wait for the element to be present on the page
    element_locator = (By.NAME,'user[email]')

    # If the element is found, print a success message
    print("Element is present on the page.")
    # Log in using a registered account 
    name = driver.find_element(By.NAME,'user[email]').send_keys('ahmed123@gmail.com')
    password = driver.find_element(By.NAME,'user[password]').send_keys('ahmed123')
    login = driver.find_element(By.NAME,'commit').click()

except Exception as e:
    # If the element is not found within the specified time, print an error message
    print(f"Element not found within 10 seconds: {e}")


finally:
    # Wait windows for 5 second before closing
    time.sleep(5)
    # Close the browser window
    driver.quit()
