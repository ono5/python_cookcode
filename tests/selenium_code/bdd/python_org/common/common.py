from selenium.webdriver.common.keys import Keys

LOG_PATH = '/Users/hono/Desktop/python_cookcode'


def get_screen_shot(description, page):
    # スクリーンショットを取得
    page.webdriver.get_screenshot_as_file(f'{LOG_PATH}/{description}.png')


def open_page(page: object) -> None:
    # 画面を開く
    page.webdriver.get(page.url)
    # 表示倍率100%
    page.body.send_keys(Keys.CONTROL + '0')
    # フルスクリーン
    page.webdriver.maximize_window()


def input_box(elem: object, content:str) -> None:
    # テキストボックスに文字を送る
    elem.send_keys(content)


def click_button(elem: object) -> None:
    elem.click()

