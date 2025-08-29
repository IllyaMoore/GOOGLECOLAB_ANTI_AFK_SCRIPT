# Google Colab Anti-AFK Script 

This project helps **keep your Google Colab session alive** by simulating user activity, preventing session timeouts during long model training or script execution.  

It is a **multi-file Python project** using **Selenium + Chromium**, and can run on Raspberry Pi, Windows, or Linux.

---

## Project Structure
```bash
colab_keeper/
│
├─ src/
│ ├─ main.py # entry point
│ ├─ config.py # settings (URL, interval, key to press)
│ ├─ browser.py # Chromium/Selenium browser setup
│ ├─ keepalive.py # activity simulation logic
│ └─ utils.py # helper functions (logging, timers)
├─ drivers/ # optional: place for chromedriver
└─ README.md
```

## Requirements

- Python 3.12+  
- Selenium (`pip install selenium`)  
- Chromium / Google Chrome  
- Chromedriver matching your browser version (or use `webdriver_manager`)  

Optional for Raspberry Pi deployment:
```bash
sudo apt update
sudo apt install chromium-browser chromium-chromedriver -y

# Clone the repository:

git clone https://github.com/IllyaMoore/GOOGLECOLAB_ANTI_AFK_SCRIPT.git
cd colab_keeper/src

# Install dependencies:

pip install -r requirements.txt

# Open src/config.py and configure:

COLAB_URL = "https://colab.research.google.com/"
INTERVAL_SEC = 240
KEY_TO_PRESS = "SHIFT"

# Run the script:

python main.py
```

