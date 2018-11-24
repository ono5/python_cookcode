from behave import *

from tests.selenium_code.flask.tests.page_model.base_page import BasePage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()


# Andが使用されたらstep
@step('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(content.driver)
    assert page.title.text == content