"""
    Main module for google_maps_scraper.
"""

import logging

import click

from google_maps_scraper.collector import GoogleMapsDataCollector


logging.basicConfig(level=logging.INFO)


@click.command()
@click.option(
    "--url",
    help="The URL of the page for which to return Google Maps results for.",
    required=True,
)
@click.option(
    "--full",
    help="An option to scrape the full page of results. Might take a while.",
    required=False,
)
def scrape_google_maps(url: str, full: bool | None = False) -> None:
    collector = GoogleMapsDataCollector()
    collector.save_maps_data(url, full)


if __name__ == "__main__":
    scrape_google_maps()
