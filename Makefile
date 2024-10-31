.PHONY: install
install:
	pip install poetry==1.8.2
	poetry install


.PHONY: scrape
scrape:
	@if [ -z "$(URL)" ]; then \
		echo 'Error: A URL of a Google Maps page is required. Use make scrape URL="<url>" [FULL="<full>"]'; \
		exit 1; \
	else \
		if [ -z "$(FULL)" ]; then \
			poetry run python -m google_maps_scraper --url="$(URL)"; \
		else \
			poetry run python -m google_maps_scraper --url="$(URL)" --full="$(FULL)"; \
		fi \
	fi
