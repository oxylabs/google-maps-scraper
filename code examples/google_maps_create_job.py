from pprint import pprint

import requests


# Structure payload.
payload = {
    "source": "google",
    "url": "https://www.google.com/maps/search/restaurants/@40.7660158,-73.9833944,14z/data=!4m5!2m4!5m2!1e0!4e9!6e5?entry=ttu",
    "geo_location": "New York,New York,United States",
    "render": "html",
}

# Get response.
response = requests.request(
    "POST",
    "https://data.oxylabs.io/v1/queries",
    auth=("USERNAME", "PASSWORD"),
    json=payload,
)

# This will return a response with job status and results url.
pprint(response.json())
