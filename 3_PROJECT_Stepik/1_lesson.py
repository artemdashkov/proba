from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(3)
driver.get("https://www.google.com/")
time.sleep(3)
driver.quit()