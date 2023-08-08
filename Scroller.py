from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Specify the path to the Chrome WebDriver executable
webdriver_path = "{Webdriver_Location}"

# Configure the Chrome WebDriver service
service = Service(webdriver_path)

# Launch the browser
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get("{URL_OF_PAGE_YOU_WANT_TO_SCROLL}")
# Wait for the page to load
time.sleep(3)

# Get the initial height of the page
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll to the bottom of the page
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(2)  # Adjust the sleep time as needed

    # Calculate the new height of the page after scrolling
    new_height = driver.execute_script("return document.body.scrollHeight")

    # Check if the page has reached the end
    if new_height == last_height:
        break

    # Update the last height
    last_height = new_height

# Close the browser
driver.quit()