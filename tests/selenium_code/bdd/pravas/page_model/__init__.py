"""page_model

画面オブジェクトの実態を定義する。

1. ページの名前に合わせて、XX_page.py ファイルを作成
例) test_login_page.py

2. XXPageという名前のクラスを作成

基本的に BasePage クラスを継承させること。

例) ベース画面クラス

class BasePage(object):
    def __init__(self, webdriver):
        self.webdriver = webdriver

    @property
    def url(self):
        return 'http://192.168.80.168'
        

例) ログイン画面クラス

class LoginPage(BasePage):
    @property
    def url(self):
        return super(LoginPage, self).url + '/login'

    @property
    def login_id(self):
        return self.webdriver.find_element(*LoginPageLocators.LOGIN_ID)


補足)
このクラスは、locators パッケージで定義したHTML要素をもとにHTML要素のオブジェクトを
取得する。

画面に新しい項目が追加されたり、削除された場合は、このページを修正すること。

ここで取得したHTML要素のオブジェクトは、scenarioパッケージで使用される。
"""