from tests.BDD.tests.acceptance.locators.home_page import HomePageLocators


class HomePage(object):

    @property
    def url(self):
        return super(HomePage, self).url + '/'

    @property
    def blog_link(self):
        return self.driver.find_element(*HomePageLocators.NAVIGATION_LINK)