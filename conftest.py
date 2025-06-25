from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import logging
import os
import pytest



def pytest_configure(config):
    if not os.path.exists('../Tensor_AQA_tasks/logs'):
        os.makedirs('../Tensor_AQA_tasks/logs')
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_file = f'../Tensor_AQA_tasks/logs/test_{current_time}.log'
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    logging.info("Test session started")

# Иницилизация дравера
@pytest.fixture(autouse=True)
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_experimental_option("prefs", {
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "download_restrictions": 0,
        "safebrowsing.enabled": False,
    })
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


