from tests.selenium_code.flask.tests.acceptance.locators.home_page import HomePageLocators
from tests.selenium_code.flask.tests.acceptance.page_model.base_page import BasePage


class HomePage(BasePage):
    @property
    def url(self):
        # basepage の http://127.0.0.1:5000 を引き継ぐ
        return super(HomePage, self).url + '/'

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGAYION_LINK)