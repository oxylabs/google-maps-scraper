import requests


# Get response.
response = requests.request(
    "GET",
    "http://data.oxylabs.io/v1/queries/{job_id}/results",
    auth=("USERNAME", "PASSWORD"),
)

# This will return the JSON response with results.
print(response.json())
