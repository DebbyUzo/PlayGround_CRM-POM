import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ActionPage.Action import Action_Page, NewCustomerActionPage, CustomerFormActionPage, SignOutActionPage
from Config.configuration import Config

@pytest.fixture(scope="session")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--headless")      # Run in headless mode
    chrome_options.add_argument("--disable-gpu")   # Prevent GPU errors in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)                     # Wait implicitly up to 20s
    driver.maximize_window()                       # Maximize window (has no effect in headless, but harmless)
    yield driver

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

def test_new_customer(login):
    new_customer = NewCustomerActionPage(login.driver)
    new_customer.click_new_customer()

def test_customer_form_page(login):
    customer_form = CustomerFormActionPage(login.driver)
    customer_form.enter_email_address(Config.EMAIL_ADDRESS)
    customer_form.enter_firstname(Config.FIRST_NAME)
    customer_form.enter_lastname(Config.LAST_NAME)
    customer_form.enter_city(Config.CITY)
    customer_form.enter_state(Config.STATE)
    customer_form.click_gender()
    customer_form.tick_add_to_promotional_list()
    customer_form.click_submit()

# Test: Sign out
def test_sign_out_page(login):
    sign_out = SignOutActionPage(login.driver)
    sign_out.click_sign_out()