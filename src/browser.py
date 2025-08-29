from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import CHROMEDRIVER_PATH

def start_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
    return driver
