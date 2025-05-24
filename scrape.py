from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import re
import time

def get_materials_data(url):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--enable-unsafe-swiftshader")

    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(15)
    driver.set_script_timeout(15)

    try:
        driver.get(url)
        time.sleep(2)

        # Get page source and save to logs.txt
        page_source = driver.page_source
        with open('logs.txt', 'w', encoding='utf-8') as file:
            file.write(page_source)

        soup = BeautifulSoup(page_source, "html.parser")
        # Return soup for further processing if needed
        return soup
        
    finally:
        driver.quit()
