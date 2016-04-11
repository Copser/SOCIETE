from selenium import webdriver
import unittest


class LiveSocieteTest(unittest.TestCase):
    """Docstring for LiveSocieteTest. Writing series of test for Societe. I'm testing
    live application on Heroku.
    """
    def setUp(self):
        """TODO: to be defined1. Define browser """
        self.browser = webdriver.Firefox()

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
        self.browser.get('http://societe.herokuapp.com/')
        self.assertIn('SOCIETE', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
