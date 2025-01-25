from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Set up the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open the URL
driver.get("https://www.centennialcollege.ca/programs-courses/full-time/artificial-intelligence-online")

# Wait for the page to load (you may need to adjust this time)
sleep(5)

# Now, you can extract the dynamically loaded content
program_details = driver.find_element(By.CSS_SELECTOR, 'span[data-component-id="pdbDetail"]')
print(program_details.text)

# Close the browser
driver.quit()