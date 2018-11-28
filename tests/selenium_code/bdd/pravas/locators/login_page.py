from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    LOGIN_ID = (By.NAME, 'id')
    LOGIN_PASSWORD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, '//input[@value="ログイン"]')
    ERROR_MESSAGE = (By.CLASS_NAME, 'alert-danger')
