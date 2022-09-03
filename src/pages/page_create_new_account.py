from selenium import webdriver
from selenium.webdriver.common.by import By


class PageCreateNewAccount:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    # user interaction elements
    first_name_input = (By.XPATH, "//input[@data-testid='firstNameInput']")
    middle_name_input = (By.XPATH, "//input[@data-testid='middleNameInput']")
    last_name_input = (By.XPATH, "//input[@data-testid='lastNameInput']")
    email_address_input = (By.XPATH, "//input[@data-testid='emailAddressInput']")
    password_input = (By.XPATH, "//input[@data-testid='passwordInput']")
    terms_of_service_checkbox = (By.XPATH, "//input[@name='tos']")
    enter_promotional_code_link = (By.XPATH, "//a[contains(text(),'Enter promotional code (optional)')]")
    promo_code_input = (By.XPATH, "//input[@data-testid='referralInput']")
    next_button = (By.XPATH, "//button[@data-testid='submitRegistration']")
    account_sign_in_link = (By.XPATH, "//a[@data-testid='register-go-to-signin']")
    create_a_business_account_link = (By.XPATH, "//a[@data-testid='register-go-to-institution-register']")

    def click_create_a_business_account(self):
        """
        Clicks create a business account link
        """
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(
            *self.create_a_business_account_link))

