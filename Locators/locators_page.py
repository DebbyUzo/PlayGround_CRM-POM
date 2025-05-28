from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME = (By.ID, "email-id")
    PASSWORD = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit-id")

class AddCustomerActionLocators:
    NEW_CUSTOMER = (By.ID, "new-customer")
    EMAIL_ADDRESS = (By.ID, "EmailAddress")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    CITY = (By.ID, "City")
    STATE = (By.ID,"StateOrRegion")
    GENDER = (By.CSS_SELECTOR, 'input[type="radio"][name="gender"][value="female"]')
    ADD_TO_PROMOTIONAL_LIST = (By.CSS_SELECTOR, "input[name='promos-name']")
    SUBMIT = (By.CSS_SELECTOR, "button.btn.btn-primary")
    SIGN_OUT = (By.CSS_SELECTOR, 'a.nav-link')


