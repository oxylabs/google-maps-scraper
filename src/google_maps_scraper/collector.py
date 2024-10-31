"""
    Main module for collecting Google Maps data.
"""

import logging

from typing import List

import pandas as pd

from google_maps_scraper.models import Location
from google_maps_scraper.scraper import GoogleMapsScraper


DEFAULT_OUTPUT_FILE = "locations.csv"


class GoogleMapsDataCollector:
    """Data collector class for Google Maps"""

    def __init__(
        self,
        output_file: str | None = None,
        logger: logging.Logger | None = None,
    ) -> None:
        self._scraper = GoogleMapsScraper()
        self._output_file = output_file if output_file else DEFAULT_OUTPUT_FILE
        self._logger = logger if logger else logging.getLogger(__name__)

    def _save_to_csv(self, locations: List[Location]) -> None:
        """Saves given list of maps items to a CSV file."""
        self._logger.info(
            f"Writing {len(locations)} locations to {self._output_file}.."
        )
        location_items = [location.model_dump() for location in locations]
        df = pd.DataFrame(location_items)
        df.to_csv(self._output_file)

    def save_maps_data(self, url: str, full: bool | None = False) -> None:
        """
        Scrapes data from Google Maps for a given query string and stores it into a CSV file.

        Args:
            url (str): The URL for the page for which to get Google Maps results.
        """
        self._logger.info(f"Getting Google Maps data for url {url}")
        try:
            items = self._scraper.get_maps_data(url, full)
        except Exception:
            self._logger.exception(f"Error when scraping Google Maps for url {url}.")
            return

        if not items:
            self._logger.info("No locations found for query.")
            return

        self._save_to_csv(items)
