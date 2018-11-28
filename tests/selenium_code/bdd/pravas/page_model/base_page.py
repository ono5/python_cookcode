from pravas.locators.base_page import basicPageLocators


class BasePage(object):
    """
    規定クラス

    全ての画面クラスは、このBasePageを継承すること
    """

    def __init__(self, webdriver):
        """
        画面オブジェクトの初期化

        :param webdriver: seleniumのドライバー
        """
        self.webdriver = webdriver

    @property
    def url(self):
        """
        ルートのURLを取得

        :return: ルートのURL
        """
        return 'http://192.168.80.168'

    @property
    def body(self):
        """ Login ボタン取得"""
        return self.webdriver.find_element(*basicPageLocators.BODY)