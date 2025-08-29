import time
from selenium.webdriver.common.keys import Keys
from config import INTERVAL_SEC, KEY_TO_PRESS

def press_key(driver):
    body = driver.find_element("tag name", "body")
    if KEY_TO_PRESS.upper() == "SHIFT":
        body.send_keys(Keys.SHIFT)
    elif KEY_TO_PRESS.upper() == "ENTER":
        body.send_keys(Keys.ENTER)

def start_keepalive(driver):
    print("Keepalive online / interval", INTERVAL_SEC, "seconds")
    while True:
        try:
            press_key(driver)
            print("Colab online")
            time.sleep(INTERVAL_SEC)
        except Exception as e:
            print("Error:", e)
            time.sleep(10)
