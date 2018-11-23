import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PythonOrgTest(unittest.TestCase):

    # テスト関数ごとに呼び出される
    def setUp(self):
        self.driver = webdriver.Firefox()

    # テスト関数ごとに呼び出される
    def tearDown(self):
        self.driver.close()

    def test_python_org(self):
        """ テスト項目1 """
        self.driver.get('http://www.python.org')
        self.assertIn('Python', self.driver.title)
        self.driver.find_element_by_link_text('Downloads').click()

        # 画面繊維は、WebDriverWait
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'widget-title')))
        self.assertEqual('Looking for a specific release?', element.text)

        self.driver.find_element_by_link_text('Documentation').click()

        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, 'call-to-action')))
        self.assertIn('Browse the docs', element.text)

        # 検索ボックス
        element = self.driver.find_element_by_name('q')
        # 検索ボックスの中身をクリア
        element.clear()
        element.send_keys('pycon')
        element.send_keys(Keys.RETURN)


if __name__ == '__main__':
    unittest.main()