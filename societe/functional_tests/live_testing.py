from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.select import Select
import unittest


class LiveSocieteTest(unittest.TestCase):
    """Docstring for LiveSocieteTest. Writing series of test for Societe. I'm testing
    live application on Heroku.
    """
    def setUp(self):
        """TODO: to be defined1. Define browser """
        self.browser = webdriver.Firefox()
        self.browser.get('http://societe.herokuapp.com/')

    def tearDown(self):
        """TODO: Docstring for tearDown.
        :returns: close web browser

        """
        self.browser.quit()

    def test_live_societe_landing_page_title(self):
        """TODO: Docstring for test_live_societe_landing_page_title. Let's see if we can fetch are live
        societe landing_page and see if the title is ok.
        :returns: title

        """
        self.assertIn('SOCIETE', self.browser.title)

    def test_live_societe_click_and_go_to_about_page(self):
        """TODO: Docstring for test_live_societe_click_and_go_to_about_page.
        :returns: TODO

        """
        WebDriverWait(self.browser, 5).until(lambda browser:
                                             self.browser.find_element_by_xpath
                                             ('//li/a[contains(text(), "About")]')).click()
        self.assertIn('http://societe.herokuapp.com/about', self.browser.current_url)

    def test_live_societe_login_using_third_party_modal(self):
        """TODO: Docstring for test_live_societe_login_third_party_modal.
        :returns: return modal for third party authentication

        """
        dropSelect = WebDriverWait(self.browser, 20).until(
            lambda browser: (self.browser.find_element_by_css_selector('div#navbar ul li.dropdown'))).click()
        twitter_choice = dropSelect.find_element_by_name('Sign in with Twitter')
        twitter_choice.click()
        self.assertIn('http://societe.herokuapp.com/contact', self.browser.current_url)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
