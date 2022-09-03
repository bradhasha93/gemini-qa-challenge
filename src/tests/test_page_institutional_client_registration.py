import unittest

from managers import test_manager
from pages.page_sign_in import PageSignIn
from pages.page_create_new_account import PageCreateNewAccount
from pages.page_institutional_client_registration import PageInstitutionalClientRegistration
from pages.page_institutional_client_registration import CompanyType
import random
import string


class TestPageInstitutionalClientRegistration(test_manager.TestManager):

    def setUp(self):
        """
        Initialize pages that tests will use
        """
        self.p_sign_in = PageSignIn(self.driver)
        self.p_create_new_account = PageCreateNewAccount(self.driver)
        self.p_institutional_client_registration = PageInstitutionalClientRegistration(self.driver)

    def go_to_form(self):
        """
        Go to institutional client registration form from sign in page
        :return:
        """
        self.openBaseUrl()
        self.p_sign_in.click_create_new_account()
        self.p_create_new_account.click_create_a_business_account()

    def execute_data_validation_scenarios(self, scenarios):
        """
        Process list of data validation scenarios provided
        :param scenarios:
        """

        # Iterate over each scenario in list provided
        for scenario_name, value_to_test, input_element, expected_element in scenarios:

            # Treat each scenario as it's own test using subTest and set subTest name to scenario_name
            with self.subTest(scenario_name):
                # Go to the institutional client registration form
                self.go_to_form()

                # Populate the form
                self.p_institutional_client_registration.populate_form(input_element, value_to_test)

                # If we are testing country_dropdown and the country is not United States,
                # verify that State dropdown is not visible
                if input_element is not None and input_element == \
                        self.p_institutional_client_registration.country_of_business_dropdown \
                        and value_to_test != "United States":
                    self.assertTrue(
                        len(self.driver.find_elements(
                            *self.p_institutional_client_registration.state_dropdown)) == 0,
                        "State dropdown is visible")

                # After populating form, click continue button to submit
                self.p_institutional_client_registration.click_continue_button()

                # Evaluate the scenario result by checking if expected_element exists
                # If expected_element exists then scenario passes, otherwise scenario fails
                self.evaluate_scenario_for_expected_element(scenario_name, value_to_test, expected_element)

    def test_legal_business_name_positive(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            ("Valid Business Name",
             "Valid Legal Business Name",
             self.p_institutional_client_registration.legal_business_name_input,
             self.p_institutional_client_registration.success_msg),

            ("Business Name with Special Character [!]",
             "Special Character Name!",
             self.p_institutional_client_registration.legal_business_name_input,
             self.p_institutional_client_registration.success_msg),

            ("Business Name with Special Character [@]",
             "Special Character Name@",
             self.p_institutional_client_registration.legal_business_name_input,
             self.p_institutional_client_registration.success_msg),

            ("Business Name with Special Character [#]",
             "Special Character Name#",
             self.p_institutional_client_registration.legal_business_name_input,
             self.p_institutional_client_registration.success_msg),

            ("Business Name with Special Character [$]",
             "Special Character Name$",
             self.p_institutional_client_registration.legal_business_name_input,
             self.p_institutional_client_registration.success_msg),

            ("Business Name with Special Character [%]",
             "Special Character Name%",
             self.p_institutional_client_registration.legal_business_name_input,
             self.p_institutional_client_registration.success_msg),

            ("Business Name with Special Character [^]",
             "Special Character Name^",
             self.p_institutional_client_registration.legal_business_name_input,
             self.p_institutional_client_registration.success_msg),

            ("Business Name with Special Character [&]",
             "Special Character Name&",
             self.p_institutional_client_registration.legal_business_name_input,
             self.p_institutional_client_registration.success_msg),

            ("Business Name with Special Character [*]",
             "Special Character Name*",
             self.p_institutional_client_registration.legal_business_name_input,
             self.p_institutional_client_registration.success_msg),

            ("Business Name with Special Character [(]",
             "Special Character Name(",
             self.p_institutional_client_registration.legal_business_name_input,
             self.p_institutional_client_registration.success_msg),

            ("Business Name with Special Character [)]",
             "Special Character Name)",
             self.p_institutional_client_registration.legal_business_name_input,
             self.p_institutional_client_registration.success_msg),
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_legal_business_name_negative(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            ("No Business Name",
             "",
             self.p_institutional_client_registration.legal_business_name_input,
             self.p_institutional_client_registration.error_msg_legal_business_name_is_required),
            ("Really Long Business Name 200 char",
             "".join(random.choices(string.ascii_uppercase + string.digits, k=200)),
             self.p_institutional_client_registration.legal_business_name_input,
             self.p_institutional_client_registration.error_msg_legal_business_name_is_required),
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_company_type_positive(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            (CompanyType.BROKER_DEALER.name,
             CompanyType.BROKER_DEALER.value,
             self.p_institutional_client_registration.company_type_dropdown,
             self.p_institutional_client_registration.success_msg),

            (CompanyType.MONEY_SERVICES_BUSINESS_OR_MONEY_TRANSMITTER.name,
             CompanyType.MONEY_SERVICES_BUSINESS_OR_MONEY_TRANSMITTER.value,
             self.p_institutional_client_registration.company_type_dropdown,
             self.p_institutional_client_registration.success_msg),

            (CompanyType.NON_PROFIT_ORGANIZATION.name,
             CompanyType.NON_PROFIT_ORGANIZATION.value,
             self.p_institutional_client_registration.company_type_dropdown,
             self.p_institutional_client_registration.success_msg),

            (CompanyType.OPERATING_COMPANY.name,
             CompanyType.OPERATING_COMPANY.value,
             self.p_institutional_client_registration.company_type_dropdown,
             self.p_institutional_client_registration.success_msg),

            (CompanyType.PERSONAL_PRIVATE_INVESTMENT_VEHICLE.name,
             CompanyType.PERSONAL_PRIVATE_INVESTMENT_VEHICLE.value,
             self.p_institutional_client_registration.company_type_dropdown,
             self.p_institutional_client_registration.success_msg),

            (CompanyType.POOLED_INVESTMENT_FUND.name,
             CompanyType.POOLED_INVESTMENT_FUND.value,
             self.p_institutional_client_registration.company_type_dropdown,
             self.p_institutional_client_registration.success_msg),

            (CompanyType.PROFESSIONAL_SERVICE_PROVIDER.name,
             CompanyType.PROFESSIONAL_SERVICE_PROVIDER.value,
             self.p_institutional_client_registration.company_type_dropdown,
             self.p_institutional_client_registration.success_msg),

            (CompanyType.PROFIT_SHARING_PENSION_RETIREMENT_PLAN.name,
             CompanyType.PROFIT_SHARING_PENSION_RETIREMENT_PLAN.value,
             self.p_institutional_client_registration.company_type_dropdown,
             self.p_institutional_client_registration.success_msg),

            (CompanyType.PUBLICLY_TRADED_COMPANY.name,
             CompanyType.PUBLICLY_TRADED_COMPANY.value,
             self.p_institutional_client_registration.company_type_dropdown,
             self.p_institutional_client_registration.success_msg),

            (CompanyType.REGISTERED_INVESTMENT_FIRM.name,
             CompanyType.REGISTERED_INVESTMENT_FIRM.value,
             self.p_institutional_client_registration.company_type_dropdown,
             self.p_institutional_client_registration.success_msg),

            (CompanyType.TRUST.name,
             CompanyType.TRUST.value,
             self.p_institutional_client_registration.company_type_dropdown,
             self.p_institutional_client_registration.success_msg),

            (CompanyType.OTHER.name,
             CompanyType.OTHER.value,
             self.p_institutional_client_registration.company_type_dropdown,
             self.p_institutional_client_registration.success_msg),
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_company_type_negative(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            ("No Company Type",
             "",
             self.p_institutional_client_registration.company_type_dropdown,
             self.p_institutional_client_registration.error_msg_company_type_is_required),

            ("Invalid Company Type option",
             "Not a valid option",
             self.p_institutional_client_registration.company_type_dropdown,
             self.p_institutional_client_registration.error_msg_company_type_is_required)
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_country_of_business_positive_us(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            ("United States",
             "United States",
             self.p_institutional_client_registration.country_of_business_dropdown,
             self.p_institutional_client_registration.success_msg)
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_country_of_business_positive_non_us(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            ("Non-US Algeria",
             "Algeria",
             self.p_institutional_client_registration.country_of_business_dropdown,
             self.p_institutional_client_registration.success_msg),

            ("Non-US Cambodia",
             "Cambodia",
             self.p_institutional_client_registration.country_of_business_dropdown,
             self.p_institutional_client_registration.success_msg),

            ("Non-US Croatia",
             "Croatia",
             self.p_institutional_client_registration.country_of_business_dropdown,
             self.p_institutional_client_registration.success_msg)
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_country_of_business_negative(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            ("No Country of Business",
             "",
             self.p_institutional_client_registration.country_of_business_dropdown,
             self.p_institutional_client_registration.generic_error_msg),

            ("Invalid Country of Business option",
             "Not a valid option",
             self.p_institutional_client_registration.country_of_business_dropdown,
             self.p_institutional_client_registration.generic_error_msg)
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_state_positive(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            ("AK",
             "AK",
             self.p_institutional_client_registration.state_dropdown,
             self.p_institutional_client_registration.success_msg),

            ("CA",
             "CA",
             self.p_institutional_client_registration.state_dropdown,
             self.p_institutional_client_registration.success_msg),

            ("NY",
             "NY",
             self.p_institutional_client_registration.state_dropdown,
             self.p_institutional_client_registration.success_msg),
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_state_negative(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            ("No State",
             "",
             self.p_institutional_client_registration.state_dropdown,
             self.p_institutional_client_registration.error_msg_company_state_is_required),

            ("Invalid State",
             "Invalid State Option",
             self.p_institutional_client_registration.state_dropdown,
             self.p_institutional_client_registration.error_msg_company_state_is_required)
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_legal_first_name_positive(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            ("Claudia",
             "Claudia",
             self.p_institutional_client_registration.legal_first_name_input,
             self.p_institutional_client_registration.success_msg),

            ("Marthaandumdaudwhahj",
             "Marthaandumdaudwhahj",
             self.p_institutional_client_registration.legal_first_name_input,
             self.p_institutional_client_registration.success_msg),
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_legal_first_name_negative(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            ("No Legal First Name",
             "",
             self.p_institutional_client_registration.legal_first_name_input,
             self.p_institutional_client_registration.error_msg_first_name_is_required),

            ("Really Long Legal First Name",
             "".join(random.choices(string.ascii_uppercase, k=200)),
             self.p_institutional_client_registration.legal_first_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal First Name with Digits",
             "Martha32872828",
             self.p_institutional_client_registration.legal_first_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal First Name with Special Character [!]",
             "Special Character Name!",
             self.p_institutional_client_registration.legal_first_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal First Name with Special Character [@]",
             "Special Character Name@",
             self.p_institutional_client_registration.legal_first_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal First Name with Special Character [#]",
             "Special Character Name#",
             self.p_institutional_client_registration.legal_first_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal First Name with Special Character [$]",
             "Special Character Name$",
             self.p_institutional_client_registration.legal_first_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal First Name with Special Character [%]",
             "Special Character Name%",
             self.p_institutional_client_registration.legal_first_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal First Name with Special Character [^]",
             "Special Character Name^",
             self.p_institutional_client_registration.legal_first_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal First Name with Special Character [&]",
             "Special Character Name&",
             self.p_institutional_client_registration.legal_first_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal First Name with Special Character [*]",
             "Special Character Name*",
             self.p_institutional_client_registration.legal_first_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal First Name with Special Character [(]",
             "Special Character Name(",
             self.p_institutional_client_registration.legal_first_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal First Name with Special Character [)]",
             "Special Character Name)",
             self.p_institutional_client_registration.legal_first_name_input,
             self.p_institutional_client_registration.generic_error_msg),
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_legal_middle_name_positive(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            ("No Legal Middle Name",
             "",
             self.p_institutional_client_registration.legal_middle_name_input,
             self.p_institutional_client_registration.success_msg),

            ("Marie",
             "Marie",
             self.p_institutional_client_registration.legal_middle_name_input,
             self.p_institutional_client_registration.success_msg),

            ("Marthaandumdaudwhahj",
             "Marthaandumdaudwhahj",
             self.p_institutional_client_registration.legal_middle_name_input,
             self.p_institutional_client_registration.success_msg),
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_legal_middle_name_negative(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            ("Really Long Legal Middle Name",
             "".join(random.choices(string.ascii_uppercase, k=200)),
             self.p_institutional_client_registration.legal_middle_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Middle Name with Digits",
             "Martha32872828",
             self.p_institutional_client_registration.legal_middle_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Middle Name with Special Character [!]",
             "Special Character Name!",
             self.p_institutional_client_registration.legal_middle_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Middle Name with Special Character [@]",
             "Special Character Name@",
             self.p_institutional_client_registration.legal_middle_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Middle Name with Special Character [#]",
             "Special Character Name#",
             self.p_institutional_client_registration.legal_middle_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Middle Name with Special Character [$]",
             "Special Character Name$",
             self.p_institutional_client_registration.legal_middle_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Middle Name with Special Character [%]",
             "Special Character Name%",
             self.p_institutional_client_registration.legal_middle_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Middle Name with Special Character [^]",
             "Special Character Name^",
             self.p_institutional_client_registration.legal_middle_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Middle Name with Special Character [&]",
             "Special Character Name&",
             self.p_institutional_client_registration.legal_middle_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Middle Name with Special Character [*]",
             "Special Character Name*",
             self.p_institutional_client_registration.legal_middle_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Middle Name with Special Character [(]",
             "Special Character Name(",
             self.p_institutional_client_registration.legal_middle_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Middle Name with Special Character [)]",
             "Special Character Name)",
             self.p_institutional_client_registration.legal_middle_name_input,
             self.p_institutional_client_registration.generic_error_msg),
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_legal_last_name_positive(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            ("Maddox",
             "Maddox",
             self.p_institutional_client_registration.legal_last_name_input,
             self.p_institutional_client_registration.success_msg),

            ("Marthaandumdaudwhahj",
             "Marthaandumdaudwhahj",
             self.p_institutional_client_registration.legal_last_name_input,self.p_institutional_client_registration.legal_last_name_input,
             self.p_institutional_client_registration.success_msg),
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_legal_last_name_negative(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            ("No Legal Last Name",
             "",
             self.p_institutional_client_registration.legal_last_name_input,
             self.p_institutional_client_registration.error_msg_last_name_is_required),

            ("Really Long Legal Last Name",
             "".join(random.choices(string.ascii_uppercase, k=200)),
             self.p_institutional_client_registration.legal_last_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Last Name with Digits",
             "Martha32872828",
             self.p_institutional_client_registration.legal_last_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Last Name with Special Character [!]",
             "Special Character Name!",
             self.p_institutional_client_registration.legal_last_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Last Name with Special Character [@]",
             "Special Character Name@",
             self.p_institutional_client_registration.legal_last_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Last Name with Special Character [#]",
             "Special Character Name#",
             self.p_institutional_client_registration.legal_last_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Last Name with Special Character [$]",
             "Special Character Name$",
             self.p_institutional_client_registration.legal_last_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Last Name with Special Character [%]",
             "Special Character Name%",
             self.p_institutional_client_registration.legal_last_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Last Name with Special Character [^]",
             "Special Character Name^",
             self.p_institutional_client_registration.legal_last_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Last Name with Special Character [&]",
             "Special Character Name&",
             self.p_institutional_client_registration.legal_last_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Last Name with Special Character [*]",
             "Special Character Name*",
             self.p_institutional_client_registration.legal_last_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Last Name with Special Character [(]",
             "Special Character Name(",
             self.p_institutional_client_registration.legal_last_name_input,
             self.p_institutional_client_registration.generic_error_msg),

            ("Legal Last Name with Special Character [)]",
             "Special Character Name)",
             self.p_institutional_client_registration.legal_last_name_input,
             self.p_institutional_client_registration.generic_error_msg),
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_email_address_positive(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            ("Claudia.Maddox@gemini.com",
             "Claudia.Maddox@gemini.com",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.success_msg),

            ("mytestemail12384738@gmail.com",
             "mytestemail12384738@gmail.com",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.success_msg),

            ("prettyandsimple@example.com",
             "prettyandsimple@example.com",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.success_msg),

            ("disposable.style.email.with+symbol@example.com",
             "disposable.style.email.with+symbol@example.com",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.success_msg),

            ("other.email-with-dash@example.com",
             "other.email-with-dash@example.com",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.success_msg),

            ("x@example.com",
             "x@example.com",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.success_msg),

            ('"much.more unusual"@example.com',
             '"much.more unusual"@example.com',
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.success_msg),

            ('"very.unusual.@.unusual.com"@example.com',
             '"very.unusual.@.unusual.com"@example.com',
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.success_msg),

            ("leading space email",
             " test@test.com",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.success_msg),

            ("trailing space email",
             "test@test.com ",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.success_msg)
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_email_address_negative(self):
        # Scenario Name, String to Test, Expected Element
        scenarios = [
            ("No Email Address",
             "",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.error_msg_enter_valid_email),

            ("Really Long Email Address",
             "".join(random.choices(string.ascii_uppercase, k=65)) + "@test.com",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.error_msg_use_valid_email),

            ("Really Long Email Domain",
             "cladogram2342342@" + "".join(random.choices(string.ascii_uppercase, k=256)) + "@test.com",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.error_msg_email_to_long),

            ("Abc.example.com",
             "Abc.example.com",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.error_msg_enter_valid_email_domain),

            ("A@b@c@example.com",
             "A@b@c@example.com",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.error_msg_use_valid_email),

            ('"a"b(c)d,e:f;gi[j\k]l@example.com',
             '"a"b(c)d,e:f;gi[j\k]l@example.com',
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.error_msg_use_symbolic_email_address_instead_of_ip_address),

            ('"very.(),:;<>[]".VERY."very@\ "very".unusual"@strange.example.com',
             '"very.(),:;<>[]".VERY."very@\ "very".unusual"@strange.example.com',
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.error_msg_use_symbolic_email_address_instead_of_ip_address),

            ("admin@mailserver1",
             "admin@mailserver1",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.error_msg_enter_valid_email_domain),

            ("user@[IPv6:2001:db8::1]@test.com",
             "user@[IPv6:2001:db8::1]@test.com",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.error_msg_use_symbolic_email_address_instead_of_ip_address),

            ('just"not"right@example.com',
             'just"not"right@example.com',
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.error_msg_use_valid_email),

            ('this is"not\allowed@example.com',
             'this is"not\allowed@example.com',
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.error_msg_use_valid_email),

            ('this\ still\"not\allowed@example.com',
             'this\ still\"not\allowed@example.com',
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.error_msg_use_valid_email),

            ("john..doe@example.com",
             "john..doe@example.com",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.error_msg_use_valid_email),

            ("john.doe@example..com",
             "john.doe@example..com",
             self.p_institutional_client_registration.your_email_address_input,
             self.p_institutional_client_registration.error_msg_use_valid_email)
        ]

        self.execute_data_validation_scenarios(scenarios)

    def test_recaptcha(self):
        self.go_to_form()
        self.assertTrue(len(self.driver.find_elements(
            *self.p_institutional_client_registration.recaptcha)) == 0
                        , "reCAPTCHA is visible")


if __name__ == '__main__':
    unittest.main()
