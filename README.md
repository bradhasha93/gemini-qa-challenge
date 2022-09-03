# gemini-qa-challenge-python setup

## Dependencies
* Python: v3.10.0
* Selenium: v4.0.0
* chromedriver: v94.0.4606.61
* geckodriver: v0.30.0
* msedgedriver: v94.0.992.50
* **Note:** For each driver, the version needed depends on your current installed respective browser version.

## Installation
1. Download Python v3.10.0 from [here](https://www.python.org/downloads/release/python-3100/)
2. Run through the Python installation
3. Open Command Prompt
4. Run `python --version` and verify result is `Python 3.10.0`
5. Run `pip install -U selenium`
6. Run `pip show selenium` and verify `Version: 4.0.0`
7. Download the latest selenium drivers to match your browser version
   1. [Download chromedriver (Google Chrome Browser)](https://chromedriver.chromium.org/downloads)
   2. [Download geckodriver (Mozilla Firefox Browser)](https://github.com/mozilla/geckodriver/releases)
   3. [Download edgedriver (Microsoft Edge Browser)](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
8. Place the drivers all into a single directory, i.e. *C:\Users\Brad\Documents\projects\selenium-drivers*
9. Add the driver directory to your PATH environment variable

## Test Execution
1. To change the test execution browser, modify `browser` in `main_config.py`
   1. The options are `edge`, `firefox`, or `chrome`
2. Open Command Prompt
3. Navigate to the `src` directory of the project
4. Execute `python -m tests.test_page_institutional_client_registration` to begin test execution


