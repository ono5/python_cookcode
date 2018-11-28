import unittest

from pyunitreport import HTMLTestRunner
from selenium import webdriver

from pravas.common.common import open_page, input_text_box, click_button, get_screen_shot
from pravas.common.common import LOGIN_PASSWORD, LOGIN_PATH
from pravas.page_model.login_page import LoginPage


class LoginPageTest(unittest.TestCase):

    def setUp(self):
        """webドライバを取得"""
        self.webdriver = webdriver.Chrome()
        # self.webdriver = webdriver.Firefox()
        # self.webdriver = webdriver.Ie()
        # self.webdriver = webdriver.Edge()

    def tearDown(self):
        """Windowを閉じる"""
        self.webdriver.close()

    def test_input_invalid_login_id_and_login_error(self):
        """ログインエラーのテスト"""
        page = LoginPage(self.webdriver)
        open_page("No.1_ログイン画面を開く", page)
        input_text_box( "No.1_不正なログインIDを入力する", page, page.login_id, "invalideLoginID")
        input_text_box("No.1_正しいパスワードを入力する", page, page.login_password, LOGIN_PASSWORD)
        # ログインボタンをクリックする
        click_button("No.1_ログインボタンをクリックする", page, page.login_button)

        # エラーメッセージを取得する
        # ログインできない場合
        error_message = page.get_error_message.text

        # 期待されるエラーメッセージか否かを確認する
        self.assertEqual('ログイン出来ませんでした', error_message)
        get_screen_shot('No.1_ログイン出来ませんでした', page)


if __name__ == '__main__':

    unittest.main(warnings='ignore', testRunner=HTMLTestRunner(output=LOGIN_PATH))