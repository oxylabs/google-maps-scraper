import requests
from pprint import pprint

# Structure payload.
payload = {
    'source': 'google',
    'url': 'https://www.google.com/maps/search/Hotels/@40.7709118,-74.0011891,14z/data=!3m1!4b1!4m7!2m6!5m4!5m2!4m1!1i2!9i185!6e3?entry=ttu',
    'geo_location': 'New York,New York,United States',
    'render': 'html'
}

# Get response.
response = requests.request(
    'POST',
    'https://data.oxylabs.io/v1/queries',
    auth=('USERNAME', 'PASSWORD'),
    json=payload
)

# This will return a response with job status and results url.
pprint(response.json())
