from behave import *
from selenium import webdriver

#  matherの正規表現をサポートする
from tests.selenium_code.flask.tests.acceptance.page_model.blog_page import BlogPage
from tests.selenium_code.flask.tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')

webdriver_path = "/Users/hono/Desktop/python_cookcode/tests/selenium_code/flask/driver/chromedriver 2"


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome(webdriver_path)
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome(webdriver_path)
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url
