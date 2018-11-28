# <u>はじめに</u> 

pravas(LaLa Callポータルサイト)のテスト自動化方式を以下に示す。

# <u>1. テスト自動化</u> 
本作業におけるテスト自動化の対応範囲は、**ユーザーインターフェース(UI)**
および **データベース(DB)** とする。

## <u>1.1 技術</u> 

テスト自動化にあたり、使用する技術、バージョンを以下に示す。

|項目名|バージョン|用途 |
|:---|:---|:---|
|python|3.7.1|メイン言語|
|selenium|3.7.0|UI画面をテストするためのフレームワーク|

Selenium（セレニウム）はブラウザのオートメーションツールであり、　
自動でブラウザを操作することでWebサイトの動作のテストを行うことができる。


## <u>1.2 UIテスト自動化</u> 

LaLa Call の画面テストを行う。


### <u>1.2.1 実行環境</u>
 
テストコードは、スクリプト実行環境の差異によって、大きく影響を受けてしまうため、
以下に環境の詳細を示す。

#### <u>1.2.1.1 PC環境</u> 

PC 環境を以下に示す。 

|OS|アーキテクチャ|備考|
|:---|:---|:---|
|Windows 10 pro|x64|-|

本案件で作成する自動化テストコードは、Windows 以外の環境(Mac, Linux)では、<font color="Tomato">**起動不可**</font>となる。   

#### <u>1.2.1.2 python 環境</u> 

Python のライブラリを利用して、開発を行う。 
環境構築は [virtualenv](https://virtualenv.pypa.io/en/latest/)を使用して、端末に依存しない仮想環境を構築する。

*インストールするモジュール

|モジュール名|用途|
|:---|:---|
|selenium|seleniumモジュール|
|coverage|カバレッジ率出力モジュール|
|html-testRunner|htmlレポート出力モジュール|
|unittest-xml-reporting|xmlレポート出力モジュール|

上記のモジュールは、requirements.txt に定義する。

```text
selenium==3.7.0
coverage
html-testRunner
unittest-xml-reporting
```

virtualenv 仮想環境に入って、以下のコマンドを実行するとモジュールのインストールができる。

```bash
pip install -r requirements.txt 
```

### <u>1.2.2 Selenium ドライバ</u> 

seleniumをpython利用するためには、webドライバを準備する必要がある。
また、ブラウザの種類によって、webドライバを使い分ける必要がある。

|ブラウザ名|ドライバ名|バージョン|インストール先|
|:---|:---|:---|:---|
|Chrome|ChromeDriver|ChromeDriver 2.44|[INSTALL](https://sites.google.com/a/chromium.org/chromedriver/downloads)|
|Edge|MicrosoftWebDriver|6.17134|[INSTALL](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)|
|Firefox|geckodriver|v0.23.0|[INSTALL](https://github.com/mozilla/geckodriver/releases)|
|IE|IEDriverServer|IEDriverServer_Win32_3.9.0|[INSTALL](https://github.com/SeleniumHQ/selenium/wiki/InternetExplorerDriver)|


* Webドライバは、**python.exe と同じディレクトリ(venv > Scrips)配下に配置する必要がある** 
* 上記は、**Windows** 環境専用のドライバとなる。

### <u>1.2.3 ブラウザの基本の設定</u> 

1. 表示倍率100% 

Internet Explorer では、表示倍率が 100% でない場合、 Selenium が実行できない。 
また、画像エビデンスをとるため、表示倍率は全てのブラウザで 100% にしておく必要がある。 

2. セキュリティの設定 

Internet Explorer のブラウザを開き、「インターネットオプション」-> 「セキュリティ」タブに移行して、
以下の項目すべてに対して、**「保護モードを有効にする」** の設定が必要になる。


![alt 画像の格納パスに誤りがあります](C:/Users/exeo/pravas_auto_test/img/ie_setting.png)

## <u>1.3 DBテスト自動化</u> 
DBの入出力テストを行う。


# <u>2. パッケージ構成</u> 
パッケージは、以下の通りとなる。

|パッケージ名|用途|補足|
|:---|:---|:---|
|pravas|親パッケージ|ルートパッケージ|
|common|子パッケージ|共通定義部品パッケージ|
|locators|子パッケージ|画面部品パッケージ|
|page_model|子パッケージ|画面モデルパッケージ|
|scenario|子パッケージ|テストシナリオパッケージ|

[*pravas_auto_test参照]

[*pravas_auto_test参照]:http://localhost:63342/pravas_auto_test/docs/_build/modules.html


テストの実行は、以下のように行う。

```
pravas パッケージと同じフォルダで、コマンドラインから以下を実行する。

1. 個別に実行する

python -m unittest pravas.scenario.test_login_page

2. まとめて実行する 
python -m unittest discover

# ファイルとして実行
runner.py pravas
```

# <u>3. テスト結果</u> 

テスト結果を、ログ・画面エビデンス・レポートの形式のいずれかで残す。

## <u>3.1 ログ</u> 

テストコードの作業ログを取得する。

格納場所は、pravas パッケージと同階層に evidence/logs フォルダを作成し、
テスト画面に合わせてサブフォルダを作成し、保存する。

例) ログイン画面の場合

```bash
pravas_aut_test
 |-pravas
 |-evidence
    |-logs
        |-login_page
        |-top_page
```

## <u>3.2 画面エビデンス</u> 

画面操作のエビデンスを png 形式で取得する。

格納場所は、pravas パッケージと同階層に evidence/screen_shot フォルダを作成し、
テスト画面に合わせてサブフォルダを作成し、保存する。

```bash
pravas_aut_test
 |-pravas
 |-evidence
    |-screen_shot
        |-login_page
        |-top_page
```

尚、以下の関数で画面エビデンスを取得する。

```bash
# スクリーンショット取得関数
def get_screen_shot(description, page):
    page.webdriver.get_screenshot_as_file(f'{LOGIN_PATH}/{description}.png')
    
    
# 呼び出すとき

get_screen_shot("項目番号_イベント名", page)

例)
get_screen_shot("項目1_画面を開く", page)

```

## <u>3.3 レポート</u>


レポートの種類は、XML レポート、HTML レポート、カバレッジレポートの 3 種類あるので、
用途に合わせて取得すること。

格納場所は、pravas パッケージと同階層に evidence/reports フォルダを作成し、
テスト画面に合わせてサブフォルダを作成し、保存する。

```bash
pravas_aut_test
 |-pravas
 |-evidence
    |-reports
        |-login_page
        |-top_page
```

[unittest-xml-reporting](https://unittest-xml-reporting.readthedocs.io/en/latest/) - XML 形式でテスト結果を出力

```bash
python -m xmlrunner pravas\scenario\test_login_page.py
```

[PyUnitReport](https://github.com/HttpRunner/PyUnitReport) - HTML 形式でテスト結果を出力

```bash
python login_page_runner.py
```

[coverage](https://dev2prod.site/python/python-unittest-coverage/) - カバレッジレポートを出力

```bash
coverage run -m unittest discover

coverage report -m
```






