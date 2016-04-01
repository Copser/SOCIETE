from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    """Docstring for NewVisitorTest. SetUp new test case for SOCIETE."""
    def setUp(self):
        """TODO: We use Firefox as browser, and configuration selenium
            to wait for three second so the page can load it's self.
        :returns: it will return Firefox browser and wait for three seconds
                  so page can load up.

        """
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """TODO: Close the browser after we done test. """
        self.browser.quit()

    def test_can_start_a_page_and_retreive_it_later(self):
        """TODO: Docstring for test_can_start_a_page_and_retreive_it_later.
        :returns: Retuns SOCIETE landing page

        """
        self.browser.get('https://societe.herokuapp.com/')

        self.assertIn('SOCIETE', self.browser.title)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
