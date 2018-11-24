from behave import *
from selenium import webdriver

#  matherの正規表現をサポートする
use_step_matcher('re')

webdriver_path = "/Users/hono/Desktop/python_cookcode/tests/selenium_code/flask/driver/chromedriver 2"


@given('I am on the homepage')
def step_impl(context):
    context.browser = webdriver.Chrome(webdriver_path)
    context.browser.get('http://127.0.0.1:5000')


@then('I am on the blog page')
def setp_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert context.browser.current_url == expected_url
