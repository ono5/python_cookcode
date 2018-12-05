import unittest

from selenium import webdriver

from tests.selenium_code.bdd.python_org.page_model.home_page import HomePage
from tests.selenium_code.bdd.python_org.common.common import open_page, input_box
from multiprocessing import Pool

class HomePageTest(unittest.TestCase):

    def setUp(self):
        """webドライバを取得"""
        self.webdriver = webdriver.Firefox()

    def tearDown(self):
        """Windowを閉じる"""
        self.webdriver.close()

    def test_homepage_title_is_correct(self):
        """ホームページのタイトルを確認"""
        # ページ情報を取得
        page = HomePage(self.webdriver)
        # ページを開く
        open_page(page)
        # ページのタイトルは Python
        self.assertIn('Python', self.webdriver.title)

    def test_search_key_is_correct(self):
        """検索ボックスのテスト"""
        page = HomePage(self.webdriver)
        open_page(page)
        # 検索ボックスのデフォルト文字をクリア
        page.search_box.clear()
        # 検索文字を送る
        input_box(page.search_box, 'pycon')

    def test_multi_process(self):
        p = Pool(10)
        p.map(self.webdriver, [
            'https://www.google.co.jp',
            'http://www.yahoo.co.jp',
        ])


if __name__ == '__main__':

    unittest.main(warnings='ignore')