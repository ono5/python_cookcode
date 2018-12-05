from tests.selenium_code.bdd.python_org.locators.base_page import BasicPageLocators


class BasePage(object):
    def __init__(self, webdriver):
        self.webdriver = webdriver

    @property
    def url(self):
        return 'https://www.python.org'

    @property
    def body(self):
        return self.webdriver.find_element(*BasicPageLocators.BODY)