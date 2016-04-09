import unittest
from selenium import webdriver


class TestSignup(unittest.TestCase):
    """Docstring for TestSignup."""
    def setUp(self):
        """TODO: to be defined1. """
        self.driver = webdriver.Firefox()

    def test_signup_fire(self):
        """TODO: Docstring for test_signup_fire.
        :returns: TODO

        """
        self.driver.get('http://localhost:8000')
        self.driver.find_element_by_id('id_title').send_keys('test title')
        self.driver.find_element_by_id('id_body').send_keys('test body')
        self.driver.find_element_by_id('submit').click()
        self.assertIn('http://localhost:8000/', self.driver.current_url)

    def tearDown(self):
        """TODO: Docstring for tearDown.
        :returns: TODO

        """
        self.driver.quit


if __name__ == '__main__':
    unittest.main()
