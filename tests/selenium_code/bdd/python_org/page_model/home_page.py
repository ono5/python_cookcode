from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.selenium_code.bdd.python_org.page_model.base_page import BasePage
from tests.selenium_code.bdd.python_org.locators.home_page import HomePageLocators


class HomePage(BasePage):
    @property
    def url(self):
        #　ページのURLを取得
        return super(HomePage, self).url

    @property
    def search_box(self):
        # 検索ボックス取得
        return self.webdriver.find_element(*HomePageLocators.SEARCH_BOX)

    @property
    def download_link(self):
        # 検索ボックス取得
        return self.webdriver.find_element(*HomePageLocators.DOWNLOADS_LINK)

    # @property
    # def get_error_message(self):
    #     """
    #     エラーメッセージ取得
    #
    #     webDriverWait を使うときは、* はつけない
    #     * をつけるとタプルを展開してしまうため、引数エラーになる。
    #
    #     * をつけない場合の渡す値
    #     self, ('xpath', '//input[@value="ログイン"]')
    #
    #     * をつける場合
    #     self, 'xpath', '//input[@value="ログイン"]'
    #
    #     """
    #
    #     return WebDriverWait(self.webdriver, 5).until(
    #         EC.presence_of_element_located(HomePageLocators.ERROR_MESSAGE))