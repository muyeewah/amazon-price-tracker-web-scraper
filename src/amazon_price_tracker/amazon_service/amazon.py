# from concurrent.futures import ThreadPoolExecutor
# from operator import methodcaller


class AmazonAPI:
    """Defines the data schema and mechanism for scarping required data on amazon"""

    def __init__(
        self,
        driver,
        base_url: str,
        currency: str,
    ) -> None:
        self.driver = driver
        self.base_url = base_url
        self.currency = currency

    def navigate_to_amazon_page(self) -> None:
        """Navigates the the amazon website"""

        self.driver.get(self.base_url)

    def search_for_product(self, search_keyword: str) -> None:
        """Search for the product(s) with search keyword"""

        searchbox = self.driver.find_element("id", "twotabsearchtextbox")
        searchbox.send_keys(search_keyword)
        searchbox.submit()

    def set_price_fiter(self, min_price, max_price) -> None:
        """Sets the price filter"""

        price_filter = f"&rh=p_36%3A{min_price}00-{max_price}00"
        self.driver.get(f"{self.driver.current_url}{price_filter}")

    def get_products_urls(self) -> list:
        """Returns the url(s) for the product(s) searched for"""

        search_result_list = self.driver.find_elements("class name", "s-result-list")
        product_urls = []

        search_results = search_result_list[0].find_elements(
            "xpath",
            "//div/span/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a",
        )

        product_urls = [url.get_attribute("href") for url in search_results]
        return product_urls

    @staticmethod
    def _get_asin(product_url: str) -> str:
        """Returns the unique ASIN for each product"""

        return product_url[product_url.find("/dp/") + 4 : product_url.find("/ref")]

    def _get_asins(self, products_urls: str) -> list:
        """Returns the list of unique ASINs for all products"""

        # return [self._get_asin(product_url) for product_url in products_urls]
        return list(map(self._get_asin, products_urls))

    def _shorten_url(self, asin: str) -> str:
        """Returns the shortened URL for a product"""

        return self.base_url + "dp/" + asin

    def _get_single_product_info(self, asin: str) -> dict:
        """Returns the information for a single product"""

        product_short_url = self._shorten_url(asin)
        self.driver.get(f"{product_short_url}")
        product_title = self._get_product_title()
        product_seller = self._get_product_seller()
        product_price = self._get_product_price()

        if product_title and product_seller:
            product_info = {
                "asin": asin,
                "url": product_short_url,
                "title": product_title,
                "seller": product_seller,
                "price": product_price,
            }
            return product_info

        return None

    def get_all_products_info(self, products_urls: str) -> list:
        """Returns the list of information for all product"""

        asins = self._get_asins(products_urls)
        products_info = []

        for asin in asins:
            product_info = self._get_single_product_info(asin)

            if product_info:
                products_info.append(product_info)

        return products_info

    def _get_product_title(self) -> str:
        """Returns the title of a product"""

        product_title = self.driver.find_element("id", "productTitle").text

        if not product_title:
            raise Exception("Unable to get title of product")
        return product_title

    def _get_product_seller(self) -> str:
        """Returns the seller of a product"""

        product_seller = self.driver.find_element("id", "bylineInfo").text
        product_seller_url = self.driver.find_element("id", "bylineInfo").get_attribute(
            "href"
        )

        if not product_seller_url:
            raise Exception("Unable to get seller of product")
        return product_seller_url

    def _get_product_price(self) -> str:
        """Returns the price of a product"""

        try:
            product_price = f'{self.driver.find_element("class name", "a-price-whole").text}.{self.driver.find_element("class name", "a-price-fraction").text}'
        except Exception:
            product_price = "Price unavailable"

        # if not product_price:
        #     raise Exception("Unable to get price of product")

        return product_price
