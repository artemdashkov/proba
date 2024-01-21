import time

from elements import ButtonsOnPageLocators
from datetime import datetime
from selenium.webdriver.common.by import By

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

link = "https://capital.com/trade-cac"
class Test2:

    def test_02(self, browser):

        global link
        # browser.set_page_load_timeout(20)
        browser.set_page_load_timeout(55)
        time_before_get_link = datetime.now()
        browser.get(link)
        time_after_get_link = datetime.now()
        time_load_page = time_after_get_link - time_before_get_link

        # current_tab = ButtonsOnPageLocators.TAB_TRADING_ITEM_MOST_TRADED  # name of Tab_1
        locator = ButtonsOnPageLocators.BUTTON_TRADING_SELL_MOST_TRADED  # button Sell (29-31 pieces)
        # item = ButtonsOnPageLocators.SPAN_TRADING_ITEM_MOST_TRADED  # name of elements
        show_all = ButtonsOnPageLocators.SHOW_ALL

        button_list = browser.find_elements(*locator)
        time.sleep(3)
        show_all_button = browser.find_element(*show_all)
        time.sleep(3)
        browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            show_all_button
        )
        time.sleep(3)
        show_all_button.click()
        time.sleep(5)
        browser.execute_script(
            'return arguments[0].scrollIntoView({block: "center", inline: "nearest"});',
            button_list[14]
        )
        time.sleep(5)
        button_list[14].click()
        time.sleep(5)

        print(f"\nКоличество кнопок: {len(button_list)}")
        print(f"time to load page: {time_load_page}")
