from selenium import webdriver
from selenium.webdriver.common.by import By


class PageSignIn:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    # user interaction elements
    email_address_input = (By.XPATH, "//input[@name='email']")
    password_input = (By.XPATH, "//input[@name='password']")
    sign_in_button = (By.XPATH, "//button[contains(., 'Sign in')]")
    create_new_account_link = (By.XPATH, "//a[@data-testid='goToRegister']")

    def send_input_email(self, email_address: str):
        """
        Populates email address on page
        :param email_address: str
        """
        self.driver.find_element(*self.email_address_input).send_keys(email_address)

    def send_input_password(self, password: str):
        """
        Populates password on page
        :param password: str
        """
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_sign_in(self):
        """
        Clicks sign in button on page
        """
        self.driver.find_element(*self.sign_in_button).click()

    def click_create_new_account(self):
        """
        Clicks create new account link
        """
        self.driver.find_element(*self.create_new_account_link).click()
