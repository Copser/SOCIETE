from selenium import webdriver
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import unittest


class SocietePageTest(unittest.TestCase):
    """Docstring for SocietePageTest. Start to write selenium testing for SOCIETE application.
    We will cover some basic stuff on the landing page, as the login, contact page, etc.
    """
    def setUp(self):
        """TODO: to be defined1.Defing what browser we are using. """
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """TODO: Docstring for tearDown.
        :returns: Quit browser afther tests

        """
        self.browser.quit()

    def test_societe_landing_page_return_title(self):
        """TODO: Docstring for test_societe_landing_page_return_title.
        :returns: Returns landing page title

        """
        self.browser.get('http://localhost:8000')

        # test is this the title
        self.assertIn('SOCIETE', self.browser.title)

    def test_societe_navbar_get_user_to_about_page(self):
        """TODO: Docstring for test_societe_navbar_get_user_to_about_page.
        :returns: Click on navbar and return about page

        """
        self.browser.get('http://localhost:8000')
        WebDriverWait(self.browser, 10).until(lambda browser:
                                              self.browser.find_element_by_xpath
                                              ('//li/a[contains(text(), "About")]')).click()
        self.assertIn('http://localhost:8000/about', self.browser.current_url)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
