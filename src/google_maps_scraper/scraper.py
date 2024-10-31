"""
    Module for scraping Google Maps.
"""

import logging
import time

from typing import List

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from google_maps_scraper.models import Location


logging.getLogger("WDM").setLevel(logging.ERROR)


class ConsentFormAcceptError(BaseException):
    message = "Unable to accept Google consent form."


class DriverInitializationError(BaseException):
    message = "Unable to initialize Chrome webdriver for scraping."


class DriverGetMapsDataError(BaseException):
    message = "Unable to get Google Maps data with Chrome webdriver."


class GoogleMapsScraper:
    """Class for scraping Google Maps"""

    def __init__(self, logger: logging.Logger | None = None) -> None:
        self._logger = logger if logger else logging.getLogger(__name__)
        self._consent_button_xpath = "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span"

    def _init_chrome_driver(self) -> webdriver.Chrome:
        """Initializes Chrome webdriver"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=chrome_options)

    def _click_consent_button(self, driver: webdriver.Chrome, url: str) -> None:
        """Clicks google consent form with selenium Chrome webdriver"""
        self._logger.info("Accepting consent form..")
        try:
            driver.get(url)
            consent_button = driver.find_element(
                By.XPATH,
                self._consent_button_xpath,
            )
            consent_button.click()
        except NoSuchElementException:
            self._logger.warning("Consent form button not found.")
        except Exception as e:
            raise ConsentFormAcceptError from e

        time.sleep(2)

    def _scroll_results_container(
        self, driver: webdriver.Chrome, container: webdriver.Chrome
    ) -> None:
        last_height = driver.execute_script(
            "return arguments[0].scrollHeight", container
        )

        while True:
            driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight", container
            )
            time.sleep(2)
            new_height = driver.execute_script(
                "return arguments[0].scrollHeight", container
            )
            if new_height == last_height:
                break
            last_height = new_height

    def _get_data_from_location_div(self, div: webdriver.Chrome) -> Location:
        """Retrieves location data from a div element and returns it as an Location object."""
        title_element = div.find_element(By.CLASS_NAME, "hfpxzc")
        title = title_element.get_attribute("aria-label")
        rating = div.find_element(By.CLASS_NAME, "ZkP5Je").get_attribute("aria-label")
        url = title_element.get_attribute("href")
        return Location(title=title, rating=rating, url=url)

    def _get_locations_from_page(
        self, url: str, driver: webdriver.Chrome, full: bool | None = False
    ) -> List[Location]:
        """Retrieves location data from a Google Maps search page."""
        driver.get(url)
        time.sleep(2)

        if full:
            result_container_xpath = "//div[contains(@aria-label, 'Results for')]"  # Xpath for the results container
            results_container = driver.find_element(By.XPATH, result_container_xpath)
            self._scroll_results_container(driver, results_container)
            time.sleep(2)

        location_divs = driver.find_elements(By.CLASS_NAME, "Nv2PK")
        return [self._get_data_from_location_div(div) for div in location_divs]

    def get_maps_data(self, url: str, full: bool | None = False) -> List[Location]:
        """
        Retrieves a list of locations in Google Maps for a given URL.

        Returns:
            List[Location]: A list of Location objects.
        Raises:
            ConsentFormAcceptError: If the Google consent form cannot be accepted.
            DriverInitializationError: If the Chrome webdriver cannot be initialized.
            DriverGetLocationDataError: If the location data cannot be scraped from the Google Maps site.
        """
        self._logger.info(f"Retrieving data from Google Maps for query {url}..")
        try:
            driver = self._init_chrome_driver()
        except Exception as e:
            raise DriverInitializationError from e

        try:
            self._click_consent_button(driver, url)
        except Exception as e:
            driver.close()
            raise e

        self._logger.info("Scraping Google Maps page..")
        try:
            return self._get_locations_from_page(url, driver, full)
        except Exception as e:
            raise DriverGetMapsDataError from e
        finally:
            driver.close()
