from behave import *
from selenium import webdriver

#  matherの正規表現をサポートする
use_step_matcher('re')

webdriver_path = "/Users/hono/Desktop/python_cookcode/tests/selenium_code/flask/driver/chromedriver 2"


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome(webdriver_path)
    context.driver.get('http://127.0.0.1:5000')


@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome(webdriver_path)
    context.driver.get('http://127.0.0.1:5000/blog')

@given('ホームページを訪れる')
def step_impl(context):
    context.driver = webdriver.Chrome(webdriver_path)
    context.driver.get('http://127.0.0.1:5000')


@then('I am on the blog page')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.driver.current_url == expected_url


@then('ブログページへ画面遷移する')
def setp_impl(context):
    expected_url = 'http://localhost:5000/blog'
    assert context.driver.current_url == expected_url
