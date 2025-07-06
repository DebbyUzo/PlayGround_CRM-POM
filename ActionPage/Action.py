import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Config.configuration import Config
from Locators.locators_page import LoginLocators, NewCustomerLocators, CustomerFormLocators, SignOutLocators

class Action_Page:

    def __init__(self, driver):
        self.driver = driver

    def login_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.USERNAME))
        element.send_keys(username)
        time.sleep(Config.WAIT_TIME)

    def enter_password(self, password):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.PASSWORD))
        element.send_keys(password)
        time.sleep(Config.WAIT_TIME)

    def click_submit_button(self):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.SUBMIT_BUTTON))
        element.click()
        time.sleep(Config.WAIT_TIME)

class NewCustomerActionPage:
    def __init__(self, driver):
        self.driver = driver

    def click_new_customer(self):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(NewCustomerLocators.NEW_CUSTOMER))
        element.click()
        time.sleep(Config.WAIT_TIME)


class CustomerFormActionPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email_address(self, email_address):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CustomerFormLocators.EMAIL_ADDRESS))
        element.send_keys(email_address)
        time.sleep(Config.WAIT_TIME)

    def enter_firstname(self, first_name):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CustomerFormLocators.FIRST_NAME))
        element.send_keys(first_name)
        time.sleep(Config.WAIT_TIME)

    def enter_surname(self, last_name):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CustomerFormLocators.SUR_NAME))
        element.send_keys(last_name)
        time.sleep(Config.WAIT_TIME)

    def enter_city(self, city):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CustomerFormLocators.CITY))
        element.send_keys(city)
        time.sleep(Config.WAIT_TIME)

    def enter_state(self, state):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CustomerFormLocators.STATE))
        element.send_keys(state)
        time.sleep(Config.WAIT_TIME)

    def click_gender(self):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(CustomerFormLocators.GENDER))
        element.click()
        time.sleep(Config.WAIT_TIME)

    def click_add_to_promotional_list(self):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CustomerFormLocators.ADD_TO_PROMOTIONAL_LIST))
        element.click()
        time.sleep(Config.WAIT_TIME)

    def click_submit(self):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(CustomerFormLocators.SUBMIT))
        element.click()
        time.sleep(Config.WAIT_TIME)


class SignOutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_sign_out(self):
        element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(SignOutLocators.SIGN_OUT))
        element.click()
        time.sleep(Config.WAIT_TIME)