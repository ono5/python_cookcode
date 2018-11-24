#◾概要
python code のサンプル集

#◾一覧
・log
  - logging のサンプルコード
・test
  - selenium のサンプルコード
  
  
#◾Wiki
```text
◾Gherkin
- pycharm にインストール
- テストシナリオの記述に使用する

◾behave(https://behave.readthedocs.io/en/latest/tutorial.html)
behave package
pip install behave

◾Pycharmの設定
Python を押下
/Users/hono/anaconda3/envs/python_cookcode/bin/behave
/Users/hono/Desktop/python_cookcode/tests/selenium_code/flask/tests/acceptance

 chmod +x cmd.sh 

multirun(https://plugins.jetbrains.com/plugin/7248-multirun)

◾Property
@property をつけると関数をプロパティ化できる

◾重複の削除方法
acceptance 配下に以下のフォルダとファイルを用意
locators(HTML要素の場所を設定)
 - base_page.py
   - HTML要素の場所をタプルで設定(TITLE = By.TAG_NAME, 'h1')
 - home_page.py
   - HTML要素の場所をタプルで設定(NAVIGATION_LINK = By.ID, 'blog-link')
 
page_model(ページの基本設定, pageのオブジェクトを作る)
 - base_page.py
   - driverの準備
   - ルートディレクトリ設定
   - ルートディレクトリのタイトルを取得
 - home_page.py
   - base_page.py を継承
   - 別のページをテスト
   
   
 
 

```