from abc import ABC, abstractmethod


class ReporterInterface(ABC):
    """This class declares the interface for the creation and attributes of a reporter"""

    @abstractmethod
    def _(self, ):
        """This methhod creates a webdriver with a set of options"""

    @abstractmethod
    def _(self, ):
        """This method sets the webdriver options"""
