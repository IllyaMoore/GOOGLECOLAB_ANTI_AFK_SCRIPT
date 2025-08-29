from browser import start_browser
from keepalive import start_keepalive
from config import COLAB_URL
from utils import log

def main():
    log("initing Colab Keeper")
    driver = start_browser()
    driver.get(COLAB_URL)

    log("loging in your account and open your notebook, then press Enter here...")
    input()

    start_keepalive(driver)

if __name__ == "__main__":
    main()
