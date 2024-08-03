# test_script.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_capture_data():
    # Setup the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Navigate to the website
        driver.get('https://example.com')
        
        # Capture data from the website
        element = driver.find_element(By.TAG_NAME, 'h1')
        print(f"Captured Text: {element.text}")
        
    finally:
        # Clean up and close the browser
        driver.quit()

if __name__ == "__main__":
    test_capture_data()
