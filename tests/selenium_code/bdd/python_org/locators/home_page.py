from selenium.webdriver.common.by import By

from tests.selenium_code.bdd.python_org.locators.base_page import BasicPageLocators


class HomePageLocators(BasicPageLocators):
    # 検索ボックス
    SEARCH_BOX = (By.NAME, 'q')
    # Downloads リンク
    DOWNLOADS_LINK = (By.LINK_TEXT, 'downloads')
