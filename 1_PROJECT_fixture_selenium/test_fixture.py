import time
from selenium.webdriver.common.by import By

link = "https://www.google.com/"

class TestSuite:
    def test_01(self, browser):
        print('start test_01')
        print("browser get link")
        browser.get(link)
        time.sleep(3)
        print("browser quit")
        browser.quit()
