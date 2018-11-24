from selenium.webdriver.common.by import By


class BlogPageLocators(object):
    ADD_POST_LINK = (By.ID, 'add-post-link')
    POSTS_SECTION = (By.ID, 'posts')
    POST = (BY.CLASS_NAME, 'post-link')