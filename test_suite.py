import pytest
from selenium import webdriver

from ActionPage.Action import Action_Page, AddCustomerActionPage


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
    login_page.login_url("https://automationplayground.com/crm/login.html")
    return login_page

def test_login_page_on_automation_customer_service_website(login):
    login.enter_username("otolinedebbie@gmail.com")
    login.enter_password("Debbie123")
    login.click_submit_button()

def test_add_customer(login):
    add_customer = AddCustomerActionPage(login.driver)

    add_customer.click_new_customer()
    add_customer.enter_email_address()
    add_customer.enter_firstname()
    add_customer.enter_lastname()
    add_customer.enter_city()
    add_customer.enter_state()
    add_customer.click_gender()
    add_customer.click_gender()
    add_customer.tick_add_to_promotional_list()
    add_customer.click_submit()
    add_customer.click_sign_out()
