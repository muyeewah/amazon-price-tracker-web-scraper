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

    def set_web_driver_options(self, *args):
        """This method sets the chrome webdriver options"""

        options = webdriver.ChromeOptions()

        for option in args:
            options.add_argument(option)

        return options
