from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from enum import Enum


class PageInstitutionalClientRegistration:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    # user interaction elements
    join_an_existing_institutional_account_link = (By.XPATH, "//a[contains(.,'Join an existing')]")
    legal_business_name_input = (By.XPATH, "//input[@name='company.legalName']")
    company_type_dropdown = (By.ID, "companyTypeDropdown")
    country_of_business_dropdown = (By.ID, "countryDropdown")
    state_dropdown = (By.ID, "stateDropdown")
    legal_first_name_input = (By.XPATH, "//input[@name='personal.legalName.firstName']")
    legal_middle_name_input = (By.XPATH, "//input[@name='personal.legalName.middleName']")
    legal_last_name_input = (By.XPATH, "//input[@name='personal.legalName.lastName']")
    your_email_address_input = (By.XPATH, "//input[@name='personal.email']")
    continue_button = (By.XPATH, "//button[@data-testid='InstitutionSubmit']")
    close_alert_link = (By.XPATH, "//div[@class='AlertClose']/a")

    # validation elements
    error_msg_legal_business_name_is_required = (By.XPATH, "//div[@class='AlertBody']//li[.='Legal Business Name is "
                                                           "required.']")
    error_msg_company_type_is_required = (By.XPATH, "//div[@class='AlertBody']//li[.='Company type is required.']")
    error_msg_first_name_is_required = (By.XPATH, "//div[@class='AlertBody']//li[.='First name is required.']")
    error_msg_last_name_is_required = (By.XPATH, "//div[@class='AlertBody']//li[.='Last name is required.']")
    error_msg_enter_valid_email = (By.XPATH, "//div[@class='AlertBody']//li[.='Please enter a valid email "
                                             "address.']")
    error_msg_use_valid_email = (By.XPATH, "//div[@class='AlertBody'][.='Please use a valid email address.']")
    error_msg_email_to_long = (By.XPATH, "//div[@class='AlertBody'][.='Please enter an email address less than "
                                         "255 characters.']")
    error_msg_enter_valid_email_domain = (By.XPATH, "//div[@class='AlertBody'][.='Please specify a valid email "
                                                    "domain.']")
    error_msg_use_symbolic_email_address_instead_of_ip_address = (By.XPATH, "//div[@class='AlertBody'][.='Please use "
                                                                            "a symbolic email address instead of an "
                                                                            "IP address.']")
    error_msg_company_state_is_required = (By.XPATH, "//div[@class='AlertBody']//li[.='Company state is required.']")
    generic_error_msg = (By.XPATH, "//div[@class='AlertBody']")
    recaptcha = (By.XPATH, "//iframe[@title='reCAPTCHA']")
    success_msg = (By.XPATH, "//h3[contains(text(),'Thanks for Registering!')]")

    def click_join_an_existing_institutional_account(self):
        """
        Clicks join an existing institutional account link
        """
        self.driver.find_element(*self.join_an_existing_institutional_account_link).click()

    def send_input_legal_business_name(self, legal_business_name: str):
        """
        Populates legal business name
        :param legal_business_name: str
        """
        element = self.driver.find_element(*self.legal_business_name_input)
        element.clear()
        element.send_keys(legal_business_name)

    def send_input_company_type(self, company_type: str):
        """
        Populates legal business name
        :param company_type: str
        """
        element = self.driver.find_element(*self.company_type_dropdown)
        element.send_keys(company_type)
        element.send_keys(Keys.ENTER)

    def send_input_country_of_business(self, country_of_business: str):
        """
        Populates country of business
        :param country_of_business: str
        """
        element = self.driver.find_element(*self.country_of_business_dropdown)
        element.send_keys(country_of_business)
        element.send_keys(Keys.ENTER)

    def send_input_state(self, state: str):
        """
        Populates state
        :param state: str
        """
        element = self.driver.find_element(*self.state_dropdown)
        element.send_keys(state)
        element.send_keys(Keys.ENTER)

    def send_input_legal_first_name(self, legal_first_name: str):
        """
        Populates legal first name
        :param legal_first_name: str
        """
        element = self.driver.find_element(*self.legal_first_name_input)
        element.clear()
        element.send_keys(legal_first_name)

    def send_input_legal_middle_name(self, legal_middle_name: str):
        """
        Populates legal middle name
        :param legal_middle_name: str
        """
        element = self.driver.find_element(*self.legal_middle_name_input)
        element.clear()
        element.send_keys(legal_middle_name)

    def send_input_legal_last_name(self, legal_last_name: str):
        """
        Populates legal last name
        :param legal_last_name: str
        """
        element = self.driver.find_element(*self.legal_last_name_input)
        element.clear()
        element.send_keys(legal_last_name)

    def send_input_your_email_address(self, your_email_address: str):
        """
        Populates your email address
        :param your_email_address: str
        """
        element = self.driver.find_element(*self.your_email_address_input)
        element.clear()
        element.send_keys(your_email_address)

    def populate_form(self, element=None, value=None):
        """
        Populate form with default values and override optionally one form data element
        :param element:
        :param value:
        """
        all_fields = dict([
            (self.legal_business_name_input, "Valid Legal Business Name"),
            (self.company_type_dropdown, CompanyType.OPERATING_COMPANY.value),
            (self.country_of_business_dropdown, "United States"),
            (self.state_dropdown, "TX"),
            (self.legal_first_name_input, "Claudia"),
            (self.legal_middle_name_input, "Marie"),
            (self.legal_last_name_input, "Maddox"),
            (self.your_email_address_input, "Claudia.Maddox@gemini.com")
        ])

        # Only override the value of an element if one is specified
        if element is not None:
            all_fields[element] = value

        # iterate over all elements and populate form
        for key, value in all_fields.items():
            match key:
                case self.legal_business_name_input:
                    self.send_input_legal_business_name(value)
                case self.company_type_dropdown:
                    self.send_input_company_type(value)
                case self.country_of_business_dropdown:
                    self.send_input_country_of_business(value)
                case self.state_dropdown:
                    if all_fields.get(self.country_of_business_dropdown) == "United States":
                        self.send_input_state(value)
                case self.legal_first_name_input:
                    self.send_input_legal_first_name(value)
                case self.legal_middle_name_input:
                    self.send_input_legal_middle_name(value)
                case self.legal_last_name_input:
                    self.send_input_legal_last_name(value)
                case self.your_email_address_input:
                    self.send_input_your_email_address(value)

    def click_continue_button(self):
        """
        Clicks continue button
        """
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(
            *self.continue_button))

    def click_close_alert(self):
        """
        Closes alert if is open
        """
        if len(self.driver.find_elements(*self.close_alert_link)) > 0:
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(
                *self.close_alert_link))


class CompanyType(Enum):
    BROKER_DEALER = "Broker-Dealer"
    MONEY_SERVICES_BUSINESS_OR_MONEY_TRANSMITTER = "Money Services Business or Money Transmitter"
    NON_PROFIT_ORGANIZATION = "Non-Profit Organization"
    OPERATING_COMPANY = "Operating Company"
    PERSONAL_PRIVATE_INVESTMENT_VEHICLE = "Personal/Private Investment Vehicle"
    POOLED_INVESTMENT_FUND = "Pooled Investment Fund (Hedge Fund, Private Equity Fund, Venture Capital Fund)"
    PROFESSIONAL_SERVICE_PROVIDER = "Professional Accounting/Law Firm"
    PROFIT_SHARING_PENSION_RETIREMENT_PLAN = "Profit Sharing/Pension/Retirement Plan (Employer-Sponsored"
    PUBLICLY_TRADED_COMPANY = "Publicly-traded Company"
    REGISTERED_INVESTMENT_FIRM = "Registered Investment Firm"
    TRUST = "Trust"
    OTHER = "Other"
