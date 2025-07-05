from selenium.webdriver.common.by import By

class LoginLocators:
      USERNAME = (By.ID, "email-id")
      PASSWORD = (By.ID, "password")
      SUBMIT_BUTTON = (By.ID, "submit-id")

class NewCustomerLocators:
      NEW_CUSTOMER = (By.ID, "new-customer")

class CustomerFormLocators:
      EMAIL_ADDRESS = (By.ID, "EmailAddress")
      FIRST_NAME = (By.ID, "FirstName")
      SUR_NAME = (By.ID, "LastName")
      CITY = (By.ID, "City")
      STATE = (By.ID,"StateOrRegion")
      GENDER = (By.NAME, "gender")
      ADD_TO_PROMOTIONAL_LIST = (By.NAME, "promos-name")
      SUBMIT = (By.XPATH, "/html/body/section/div/div/div/div/form/button")

class SignOutLocators:
      SIGN_OUT = (By.XPATH, '/html/body/nav/ul/li/a')
