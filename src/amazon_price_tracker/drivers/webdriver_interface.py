from abc import ABC, abstractmethod

class WebDriverInterface(ABC):
    """ This class declares the interface for the creation and attributes of a webdriver """

    @abstractmethod
    def create_web_driver(self, webdriver_options):
        """ This methhod creates a webdriver with a set of options """

    @abstractmethod
    def set_web_driver_options(self, *args):
        """This method sets the webdriver options"""
