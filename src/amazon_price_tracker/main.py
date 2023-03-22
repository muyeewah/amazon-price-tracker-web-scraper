import time
from drivers.chrome_webdriver import ChromeWebDriver


def test_driver_creation():

    webdriver = ChromeWebDriver()
    driver_options = webdriver.get_web_driver_options()
    webdriver.set_automation_headless_state(driver_options, "--headless")
    driver = webdriver.create_web_driver(driver_options)
    driver.get("https://www.google.com")
    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    test_driver_creation()
