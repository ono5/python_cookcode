"""locators パッケージ

画面のHTML要素をクラスとして定義する。
ここで定義したクラスは、page_model パッケージで要素の取得をする際に使用する。

1. ページの名前に合わせて、XX_page.py ファイルを作成
例) test_login_page.py

2. XXLocatorsという名前のクラスを作成

例) ログイン画面クラス

class LoginPageLocators(object):
    LOGIN_ID = (By.NAME, 'id')
    LOGIN_PASSWORD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//input[@value="ログイン"]')

補足)
このクラスは、画面のHTML要素(部品)を表す。
既に作成済みのログイン画面から以下の要素を抽出し、辞書型で定義している。

* LOGIN_ID
<input class="form-control" required="" name="id" type="text" value="">

<input class="form-control" required="" name="password" type="password" value="">

<input class="btn btn-info btn-block" formaction="http://192.168.80.168/login" type="submit" value="ログイン">


このようにテストコードからHTML部品を分離しておけば、画面修正時にHTMLのidやnameが
変わったとしても、このパッケージ内のファイルを修正すれば、テストコードの修正は不要となる。
"""