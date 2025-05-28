import pytest
from selenium import webdriver

from ActionPage.Action import Action_Page, AddCustomerActionPage
from Config.configuration import Config


@pytest.fixture(scope="session")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def login(driver_setup):
    driver = driver_setup
    login_page = Action_Page(driver)
    login_page.login_url(Config.BASE_URL)
    return login_page

def test_login_page_on_automation_customer_service_website(login):
    login.enter_username(Config.USERNAME)
    login.enter_password(Config.PASSWORD)
    login.click_submit_button()

def test_add_customer(login):
    add_customer = AddCustomerActionPage(login.driver)

    add_customer.click_new_customer()
    add_customer.enter_email_address(Config.EMAIL_ADDRESS)
    add_customer.enter_firstname(Config.FIRST_NAME)
    add_customer.enter_lastname(Config.LAST_NAME)
    add_customer.enter_city(Config.CITY)
    add_customer.enter_state(Config.STATE)
    add_customer.click_gender()
    add_customer.click_gender()
    add_customer.tick_add_to_promotional_list()
    add_customer.click_submit()
    add_customer.click_sign_out()
