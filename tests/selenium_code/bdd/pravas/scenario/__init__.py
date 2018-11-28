"""scenarioパッケージ
ここでは、テストシナリオを定義する。

1. ページの名前に合わせて、XX_page.py ファイルを作成
例) test_login_page.py

2. クラスを定義する

class LoginPageTest(unittest.TestCase):
    def setUp(self):
        self.webdriver = webdriver.Chrome(CHROME_DRIVER)
        self.webdriver.maximize_window()

    def tearDown(self):
        self.webdriver.close()

    def test_input_invalid_login_id_and_login_error(self):
        page = LoginPage(self.webdriver)
        open_page("No.1_ログイン画面を開く", page)
        input_text_box( "No.1_不正なログインIDを入力する", page, page.login_id, "invalideLoginID")
        input_text_box("No.1_正しいパスワードを入力する", page, page.login_password, LOGIN_PASSWORD)
        # ログインボタンをクリックする
        click_button("No.1_ログインボタンをクリックする", page, page.login_button)

        # エラーメッセージを取得する
        error_message = page.get_error_message.text

        # 期待されるエラーメッセージか否かを確認する
        self.assertEqual('ログイン出来ませんでした', error_message)


補足)
ここでは、page_modelから画面オブジェクトを作成し、commonに定義した関数を呼び出して、
画面テストを実行する。

また、assert 関数を定義して、テスト結果を確認する
"""