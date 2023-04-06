import time

from amazon_service.amazon import AmazonAPI
from drivers.chrome_webdriver import ChromeWebDriver
from selenium.common.exceptions import NoSuchElementException

def run_scraper():
    """Entry point to the application"""

    webdriver = ChromeWebDriver()
    driver_options = webdriver.set_web_driver_options("--start-maximized", "--headless")
    driver = webdriver.create_web_driver(driver_options)
    price_filter = {
        "min_price": "200",
        "max_price": "500"
    }
    amazon_api = AmazonAPI(driver, "http://www.amazon.co.uk/", "PS5", "")

    try:
        with driver:
            scraper_result = amazon_api.execute()
            return scraper_result
    except (NoSuchElementException, RuntimeError) as error_message:
        print(f"error_log: {error_message}")      


if __name__ == "__main__":
    start = time.time()

    results = run_scraper()
    print(results)

    end = time.time()
    print(end - start)
