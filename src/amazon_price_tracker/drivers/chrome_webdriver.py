from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from drivers.webdriver_interface import WebDriverInterface


class ChromeWebDriver(WebDriverInterface):
    """This class defines the creation and attributes of a chrome webdriver"""

    def create_web_driver(self, webdriver_options):
        """This methhod creates a chrome webdriver with a set of options"""

        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            chrome_options=webdriver_options,
        )

    def get_web_driver_options(self):
        """This method gets the chrome webdriver options"""

        return webdriver.ChromeOptions()

    def set_certificate_error_ignoring_state(
        self, options, certificate_error_ignoring_state: str
    ):
        """This method sets the certificate error ignoring state"""

        options.add_argument(certificate_error_ignoring_state)

    def set_browser_incognito_mode(self, options, incognito_mode):
        """This method sets the browser incognito mode"""

        options.add_argument(incognito_mode)

    def set_automation_headless_state(self, options, automation_headless_state):
        """This method sets the automation headless state"""

        options.add_argument(automation_headless_state)
