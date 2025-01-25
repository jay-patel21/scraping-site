from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = "https://www.centennialcollege.ca/programs-courses/full-time/artificial-intelligence-online"
driver.get(url)

time.sleep(2)  # Adjust the wait time as needed
section = driver.find_element(By.ID, "pdbTabs")

paragraphs = section.find_elements(By.TAG_NAME, "p")
if len(paragraphs) >= 2:
    print("\nFirst Paragraph:")
    print(paragraphs[0].text)

    print("\nSecond Paragraph:")
    print(paragraphs[1].text)
else:
    print("Not enough paragraphs found.")

driver.quit()