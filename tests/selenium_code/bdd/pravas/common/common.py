"""
テスト自動化で共通で使用する関数を定義する
"""

# 設定パラメータ
from selenium.webdriver.common.keys import Keys

def get_screen_shot(description, page):
    """
    スクリーンショットを取得

    :param description: 操作の説明(例 ; 画面を開く)
    :param page: 各ページのオブジェクト(例：ログインページ、ホームページ)
    :return: なし
    """
    page.webdriver.get_screenshot_as_file(f'{LOGIN_PATH}/{description}.png')


def open_page(description: str, page: object) -> None:
    """
    指定した画面を開く(表示倍率100%, フルスクリーン)

    :param description: 操作の説明(例: 画面を開く)
    :param page: ページ情報(例：ログインページ)
    :return: なし
    """
    # 画面を開く
    page.webdriver.get(page.url)
    # 表示倍率100%
    page.body.send_keys(Keys.CONTROL + '0')
    # フルスクリーン
    page.webdriver.maximize_window()
    get_screen_shot(description, page)


def input_text_box(description: str, page: object, elem: object, content:str) -> None:
    """
    テキストボックスに任意の文字列を送信する

    :param description: 操作の説明(例: 画面を開く)
    :param page: ページ情報(例：ログインページ)
    :param elem: HTML 要素
    :param contents: テキストボックスに送信する内容
    :return: なし
    """

    elem.send_keys(content)
    get_screen_shot(description, page)


def click_button(description: str, page: object, elem: object) -> None:
    """
    ボタン要素をクリックする

    :param page: ページ情報(例：ログインページ)
    :param description: description: 操作の説明(例: 画面を開く)
    :return: なし
    """

    elem.click()
    get_screen_shot(description, page)

