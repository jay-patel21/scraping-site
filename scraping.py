import requests
from bs4 import BeautifulSoup
import time
import html
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


url = "https://www.centennialcollege.ca/programs-courses/full-time/artificial-intelligence-online"


def scrape_centennial_college():
    
    # Fetch the webpage
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")
        return
    
    # Parse the webpage content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # a. Extract the title of the website
    title = soup.title.string if soup.title else "No title found"
    print("Website Title:", title)

def scrap_program_overview():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
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
    
def scrap_program_highlight():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(url)
    time.sleep(2)  # Adjust the wait time as needed  
    
    program_details = driver.find_element(By.CSS_SELECTOR, 'span[data-component-id="pdbDetail"]')
    print(program_details.text)      
    
# Run the scraper
scrape_centennial_college()
scrap_program_highlight()
scrap_program_overview()


