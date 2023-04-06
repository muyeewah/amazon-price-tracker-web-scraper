import time

from amazon_service.amazon import AmazonAPI
from drivers.chrome_webdriver import ChromeWebDriver
from selenium.common.exceptions import NoSuchElementException

def run():

    pass


def test_driver_creation():

    webdriver = ChromeWebDriver()
    driver_options = webdriver.set_web_driver_options("--start-maximized", "--headless")
    return webdriver.create_web_driver(driver_options)
    

def test_amazon_api(driver):
    
    amazonAPI = AmazonAPI(driver, "http://www.amazon.co.uk/", "")
    amazonAPI.navigate_to_amazon_page()
    amazonAPI.search_for_product("PS5")
    amazonAPI.set_price_fiter("200", "500")
    product_urls = amazonAPI.get_products_urls()
    products_info = amazonAPI.get_all_products_info(product_urls)
    print(products_info)


if __name__ == "__main__":
    start = time.time()

    try:
        with test_driver_creation() as driver:
            test_amazon_api(driver)
    except (NoSuchElementException, RuntimeError) as error_message:
        print(f"error_log: {error_message}")

    end = time.time()
    print(end - start)
