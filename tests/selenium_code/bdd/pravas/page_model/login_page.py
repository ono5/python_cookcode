from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pravas.locators.login_page import LoginPageLocators
from pravas.page_model.base_page import BasePage


class LoginPage(BasePage):
    @property
    def url(self):
        """ログイン画面の古パスを取得"""
        return super(LoginPage, self).url + '/login'

    @property
    def login_id(self):
        """Login ID 取得"""
        return self.webdriver.find_element(*LoginPageLocators.LOGIN_ID)

    @property
    def login_password(self):
        """ Password 取得"""
        return self.webdriver.find_element(*LoginPageLocators.LOGIN_PASSWORD)

    @property
    def login_button(self):
        """ Login ボタン取得"""
        return self.webdriver.find_element(*LoginPageLocators.LOGIN_BUTTON)

    @property
    def get_error_message(self):
        """
        エラーメッセージ取得

        webDriverWait を使うときは、* はつけない
        * をつけるとタプルを展開してしまうため、引数エラーになる。

        * をつけない場合の渡す値
        self, ('xpath', '//input[@value="ログイン"]')

        * をつける場合
        self, 'xpath', '//input[@value="ログイン"]'

        """

        return WebDriverWait(self.webdriver, 5).until(
            EC.presence_of_element_located(LoginPageLocators.ERROR_MESSAGE))