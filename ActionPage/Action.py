import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Locators.locators_page import LoginLocators, AddCustomerActionLocators


class Action_Page:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.USERNAME))
        enter_username.send_keys(username)
        time.sleep(15)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.PASSWORD))
        enter_password.send_keys(password)
        time.sleep(15)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.SUBMIT_BUTTON))
        click_submit_button.click()
        time.sleep(15)

class AddCustomerActionPage:
    def __init__(self, driver):
        self.driver = driver

    def click_new_customer(self):
        click_new_customer = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddCustomerActionLocators.NEW_CUSTOMER))
        click_new_customer.click()
        time.sleep(15)

    def enter_email_address(self):
        enter_email_address = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddCustomerActionLocators.EMAIL_ADDRESS))
        enter_email_address.send_keys("otolinedebbie@gmail")
        time.sleep(15)

    def enter_firstname(self):
        enter_firstname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddCustomerActionLocators.FIRST_NAME))
        enter_firstname.send_keys("Debbie")
        time.sleep(15)

    def enter_lastname(self):
        enter_lastname = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddCustomerActionLocators.LAST_NAME))
        enter_lastname.send_keys("Ego")
        time.sleep(15)

    def enter_city(self):
        enter_city = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddCustomerActionLocators.CITY))
        enter_city.send_keys("Lagos")
        time.sleep(15)

    def enter_state(self):
        enter_state = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddCustomerActionLocators.STATE))
        enter_state.send_keys("Louisiana")
        time.sleep(15)

    def click_gender(self):
        click_gender = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddCustomerActionLocators.GENDER))
        click_gender.click()
        time.sleep(15)

    def tick_add_to_promotional_list(self):
        tick_add_to_promotional_list = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddCustomerActionLocators.ADD_TO_PROMOTIONAL_LIST))
        tick_add_to_promotional_list.click()
        time.sleep(15)

    def click_submit(self):
        click_submit = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddCustomerActionLocators.SUBMIT))
        click_submit.click()
        time.sleep(15)

    def click_sign_out(self):
        click_sign_out = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(AddCustomerActionLocators.SIGN_OUT))
        click_sign_out.click()
        time.sleep(15)
