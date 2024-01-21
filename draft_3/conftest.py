import datetime
import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

import conf


@pytest.fixture(scope="session")
def browser():
    service = ChromeService(executable_path=ChromeDriverManager().install())

    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = "normal" # "eager"
    chrome_options.add_argument(conf.CHROME_WINDOW_SIZES)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument("--accept-lang=en")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_page_load_timeout(5)
    return driver


