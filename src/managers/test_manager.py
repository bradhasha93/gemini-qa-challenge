import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from config import main_config


class TestManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Setup driver instance
        """
        # Create driver instance based on value specified in main_config.py
        match main_config.browser:
            case "chrome":
                cls.driver = webdriver.Chrome()
            case "firefox":
                cls.driver = webdriver.Firefox()
            case "edge":
                cls.driver = webdriver.Edge()

        # Set base_url for driver
        cls.base_url = main_config.base_url

        # Maximize the browser window
        cls.driver.maximize_window()

        # Open base_url in browser
        cls.driver.get(cls.base_url)

    def openBaseUrl(self):
        """
        Open base url for driver
        """
        self.driver.get(self.base_url)

    def get_web_driver_wait(self, timeout: int):
        """
        Return instance of WebDriverWait with a specified timeout
        :param timeout: int
        :return: WebDriverWait(int)
        """
        return WebDriverWait(self.driver, timeout)

    def evaluate_scenario_for_expected_element(self, scenario, value_to_test, expected_element):
        """
        Evaluate scenario for expected_element
        :param scenario:
        :param value_to_test:
        :param expected_element:
        """
        try:
            # Wait default_wd_wait time for element, catch exception if element does not appear and
            # continue to assertion
            self.get_web_driver_wait(main_config.default_wd_wait).until(lambda wd: len(
                self.driver.find_elements(*expected_element)) > 0)
        except:
            print("element not located continuing to assertion")
        # Assert true if expected_element exists (Scenario Passes), otherwise assert false (Scenario Fails)
        self.assertTrue(len(self.driver.find_elements(
            *expected_element)) > 0
                        , "Expected element " + expected_element[1] +
                        " is not present: Scenario [" + scenario + "], "
                        "Test Value [" + value_to_test + "]")

    @classmethod
    def tearDownClass(cls):
        """
        Teardown the driver instance
        """
        cls.driver.quit()
