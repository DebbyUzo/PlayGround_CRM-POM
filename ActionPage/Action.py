import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Config.configuration import Config
from Locators.locators_page import LoginLocators, AddCustomerActionLocators


class Action_Page:
    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.USERNAME))
        enter_username.send_keys(username)
        time.sleep(Config.WAIT_TIME)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.PASSWORD))
        enter_password.send_keys(password)
        time.sleep(Config.WAIT_TIME)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.SUBMIT_BUTTON))
        click_submit_button.click()
        time.sleep(Config.WAIT_TIME)

class AddCustomerActionPage:
    def __init__(self, driver):
        self.driver = driver

    def click_new_customer(self):
        click_new_customer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerActionLocators.NEW_CUSTOMER))
        click_new_customer.click()
        time.sleep(Config.WAIT_TIME)

    def enter_email_address(self, email_address):
        enter_email_address = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerActionLocators.EMAIL_ADDRESS))
        enter_email_address.send_keys(email_address)
        time.sleep(Config.WAIT_TIME)

    def enter_firstname(self, first_name):
        enter_firstname = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerActionLocators.FIRST_NAME))
        enter_firstname.send_keys(first_name)
        time.sleep(Config.WAIT_TIME)

    def enter_lastname(self, last_name):
        enter_lastname = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerActionLocators.LAST_NAME))
        enter_lastname.send_keys(last_name)
        time.sleep(Config.WAIT_TIME)

    def enter_city(self, city):
        enter_city = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerActionLocators.CITY))
        enter_city.send_keys(city)
        time.sleep(Config.WAIT_TIME)

    def enter_state(self, state):
        enter_state = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerActionLocators.STATE))
        enter_state.send_keys(state)
        time.sleep(Config.WAIT_TIME)

    def click_gender(self):
        click_gender = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerActionLocators.GENDER))
        click_gender.click()
        time.sleep(Config.WAIT_TIME)

    def tick_add_to_promotional_list(self):
        tick_add_to_promotional_list = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerActionLocators.ADD_TO_PROMOTIONAL_LIST))
        tick_add_to_promotional_list.click()
        time.sleep(Config.WAIT_TIME)

    def click_submit(self):
        click_submit = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerActionLocators.SUBMIT))
        click_submit.click()
        time.sleep(Config.WAIT_TIME)

    def click_sign_out(self):
        click_sign_out = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddCustomerActionLocators.SIGN_OUT))
        click_sign_out.click()
        time.sleep(Config.WAIT_TIME)
