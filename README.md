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

◾Sphinx 
# venv を用意
python3.6 -m venv venv
# activate
source venv/bin/activate
# sphinx のインストール
(venv) $ pip install sphinx
# プロジェクトを始める(python-cookbook => document root)
sphinx-quickstart -q -p Python_Cookbook -a HIROKI -v 1.0 docs

# Mark down形式を有効にする
pip install recommonmark

# コードハイライト機能
Pygments(http://pygments.org/docs/lexers/)
pip install Pygments

# sphinx_rtd_themeをインストール
pip install sphinx_rtd_theme

# conf.pyを修正する

import os
import sys
sys.path.insert(0, os.path.abspath('../'))

source_suffix = ['.rst', '.md']
# 拡張子 .md パーサー(構文解析器)に recommonmark を指定する
source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser'
}

extensions = ['sphinx.ext.autodoc','sphinx.ext.viewcode']
# Include Python objects as they appear in source files
# Default: alphabetically ('alphabetical')
autodoc_member_order = 'bysource'
# Default flags used by autodoc directives
autodoc_default_flags = ['members', 'show-inheritance']
autodoc_mock_imports = ["django", "selenium"]

html_theme = 'sphinx_rtd_theme'

# rst ファイル作成(作成場所 ソースファイルのルート)
sphinx-apidoc -f  -o ./docs .

# rst ファイルから html ファイルを作成(rstファイル格納場所, html ファイル格納先)
sphinx-build -b html ./docs ./docs/_build

# Degital Ocean
Django Tutorial(https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-centos-7)

# pytest code sample
https://pragprog.com/titles/bopytest/source_code

```