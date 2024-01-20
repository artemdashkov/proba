import time

from elements import ButtonsOnPageLocators
from datetime import datetime

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

link = "https://capital.com/trade-cac"
class Test1:

    def test_01(self):

        global link
        time_load = []
        service = ChromeService(executable_path=ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.page_load_strategy = "normal"  # "eager" "normal" "none"
        chrome_options.add_argument("--window-size=1280,720")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_argument("--accept-lang=en")

        chrome_options.add_argument("--headless=new")

        for x in range(10):

            driver = webdriver.Chrome(service=service, options=chrome_options)
            # driver.set_page_load_timeout(60)
            # current_tab = ButtonsOnPageLocators.TAB_TRADING_ITEM_MOST_TRADED
            # locator = ButtonsOnPageLocators.BUTTON_TRADING_SELL_MOST_TRADED
            # item = ButtonsOnPageLocators.SPAN_TRADING_ITEM_MOST_TRADED

            time_before_get_link = datetime.now()
            print(f"\n {time_before_get_link} -before get(link)")

            driver.get(link)

            time_after_get_link = datetime.now()
            print(f"\n {time_after_get_link} -after get(link)")

            # button_list = driver.find_elements(*locator)

            # print(len(button_list))

            time_load_page = time_after_get_link - time_before_get_link

            print(f"time to load {time_load_page.seconds}")
            time_load.append(time_load_page.seconds)
            driver.quit()

        print(f'total time to load page {time_load}')