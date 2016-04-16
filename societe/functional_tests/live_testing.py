from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
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
        """TODO: Docstring for test_live_societe_login_third_party_modal. This test will login to
        SOCIETE using third party authentication, after that we will wait for automatic redirect to
        contact form page. We need to fill out this form.
        :returns: return modal for third party authentication, success on fill out contact form

        """
        # Fetch and click on dropdown then click on twitter login button
        dropSelect = WebDriverWait(self.browser, 20).until(
            lambda browser: (self.browser.find_element_by_css_selector('div#navbar ul li.dropdown')))
        dropSelect.click()
        twitter_choice = dropSelect.find_element_by_id('twitter_login')
        twitter_choice.click()
        # Fill out twitter oauth form
        login_form = WebDriverWait(self.browser, 5).until(
            lambda browser: (self.browser.find_element_by_id('username_or_email')))
        login_form.send_keys('')
        password_form = WebDriverWait(self.browser, 5).until(
            lambda browser: (self.browser.find_element_by_id('password')))
        password_form.send_keys('')
        # Sign in to SOCIETE, but first wait for authomatic redirection
        select_sign_in = WebDriverWait(self.browser, 5).until(
            lambda browser: (self.browser.find_element_by_id('allow')))
        select_sign_in.click()

        # Filling out the form on contact page
        # first name, last name, email, mobile
        first_name_field = WebDriverWait(self.browser, 15).until(
            lambda browser: (self.browser.find_element_by_id('id_first_name')))
        first_name_field.send_keys('John')
        last_name_field = WebDriverWait(self.browser, 15).until(
            lambda browser: (self.browser.find_element_by_id('id_last_name')))
        last_name_field.send_keys('Doe')
        email_name_field = WebDriverWait(self.browser, 15).until(
            lambda browser: (self.browser.find_element_by_id('id_email')))
        email_name_field.send_keys('johndoe@gmail.com')
        mobile_field = WebDriverWait(self.browser, 15).until(
            lambda browser: (self.browser.find_element_by_id('id_mobile')))
        mobile_field.send_keys('')

        # Birthday widget
        birthday_widget_month = WebDriverWait(self.browser, 15).until(
            lambda browser: Select(self.browser.find_element_by_id('id_birthday_month')))
        birthday_widget_month.select_by_visible_text('October')
        birthday_widget_day = WebDriverWait(self.browser, 15).until(
            lambda browser: Select(self.browser.find_element_by_id('id_birthday_day')))
        birthday_widget_day.select_by_visible_text('10')
        birthday_widget_year = WebDriverWait(self.browser, 15).until(
            lambda browser: Select(self.browser.find_element_by_id('id_birthday_year')))
        birthday_widget_year.select_by_visible_text('1992')

        # Move in date widget
        move_in_date_month = WebDriverWait(self.browser, 15).until(
            lambda browser: Select(self.browser.find_element_by_id('id_move_in_date_month')))
        move_in_date_month.select_by_visible_text('April')
        move_in_date_day = WebDriverWait(self.browser, 15).until(
            lambda browser: Select(self.browser.find_element_by_id('id_move_in_date_day')))
        move_in_date_day.select_by_visible_text('17')
        move_in_date_year = WebDriverWait(self.browser, 15).until(
            lambda browser: Select(self.browser.find_element_by_id('id_move_in_date_year')))
        move_in_date_year.select_by_visible_text('2016')

        # Move out date widget
        move_out_date_month = WebDriverWait(self.browser, 15).until(
            lambda browser: Select(self.browser.find_element_by_id('id_move_out_date_month')))
        move_out_date_month.select_by_visible_text('May')
        move_out_date_day = WebDriverWait(self.browser, 15).until(
            lambda browser: Select(self.browser.find_element_by_id('id_move_out_date_day')))
        move_out_date_day.select_by_visible_text('17')
        move_out_date_year = WebDriverWait(self.browser, 15).until(
            lambda browser: Select(self.browser.find_element_by_id('id_move_out_date_year')))
        move_out_date_year.select_by_visible_text('2016')

        # Country widget
        country_widget = WebDriverWait(self.browser, 15).until(
            lambda browser: Select(self.browser.find_element_by_id('id_country')))
        country_widget.select_by_visible_text('Serbia')

        # Message field
        message_field = WebDriverWait(self.browser, 15).until(
            lambda browser: (self.browser.find_element_by_id('id_message')))
        message_field.send_keys("Hello SOCIETE, I'm John Doe")

        # Send form
        send_form = WebDriverWait(self.browser, 15).until(
            lambda browser: (self.browser.find_element_by_xpath('//button[text()="Submit"]')))
        send_form.click()

        # assert
        self.assertIn('http://societe.herokuapp.com/success', self.browser.current_url)
        self.assertIn('http://societe.herokuapp.com/contact', self.browser.current_url)


if __name__ == '__main__':
    unittest.main(warnings='ignore')
