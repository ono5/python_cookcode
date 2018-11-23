from behave import *
from selenium import webdriver

#  matherの正規表現をサポートする
use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    browser = webdriver.Chrome("/Users/hono/Desktop/python_cookcode/tests/selenium_code/flask/driver/chromedriver 2")
    browser.get('http://127.0.0.1:5000')