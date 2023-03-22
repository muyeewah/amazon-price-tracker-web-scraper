from abc import ABC, abstractmethod

class WebDriverInterface(ABC):
    """ This class declares the interface for the creation and attributes of a webdriver """

    @abstractmethod
    def create_web_driver(self, webdriver_options):
        """ This methhod creates a webdriver with a set of options """

    @abstractmethod
    def get_web_driver_options(self):
        """This method gets the webdriver options"""

    @abstractmethod
    def set_certificate_error_ignoring_state(self, options, certificate_error_ignoring_state):
        """ This method sets the certificate error ignoring state """

    @abstractmethod
    def set_browser_incognito_mode(self, options, incognito_mode):
        """ This method sets the browser incognito mode """

    @abstractmethod
    def set_automation_headless_state(self, options, automation_headless_state):
        """ This method sets the automation headless state """
