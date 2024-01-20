from selenium import webdriver
from selenium.webdriver.common.by import By

class ButtonsOnPageLocators:
    # Tabs
    TAB_TRADING_ITEM_MOST_TRADED = (By.CSS_SELECTOR,
                                    "div.main__tab--wrap > div > a:nth-child(1)") # name of Tab_1
    TAB_TRADING_ITEM_TOP_RISERS = (By.CSS_SELECTOR,
                                   "div.main__tab--wrap > div > a:nth-child(2)") # name of Tab_2

    # Buttons
    BUTTON_TRADING_SELL_MOST_TRADED = (By.CSS_SELECTOR,
                                       ".tab-mosttraded > table > tbody > tr > td:nth-child(3) > a") # button Sell (29-31 pieces)

    SPAN_TRADING_ITEM_MOST_TRADED = (By.CSS_SELECTOR,
                                     ".table-tools.catTabs.tab-mosttraded > table > "
                                                      "tbody > tr > td.name > a > span.table-tools__title")



