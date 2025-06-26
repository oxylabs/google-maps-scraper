# Google Maps Scraper
[![Oxylabs promo code](https://raw.githubusercontent.com/oxylabs/how-to-scrape-google-scholar/refs/heads/main/Google-Scraper-API-1090x275.png)](https://oxylabs.io/products/scraper-api/serp/google?utm_source=877&utm_medium=affiliate&groupid=877&utm_content=google-maps-scraper-github&transaction_id=102c8d36f7f0d0e5797b8f26152160)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.com/invite/Pds3gBmKMH)

- [Google Maps Scraper](#google-maps-scraper)
  * [Free Google Maps Scraper](#free-google-maps-scraper)
    + [Prerequisites](#prerequisites)
    + [Installation](#installation)
    + [Getting the URL for the Maps page to scrape](#getting-the-url-for-the-maps-page-to-scrape)
    + [Scraping](#scraping)
    + [Notes](#notes)
  * [Oxylabs Google Maps Scraper](#oxylabs-google-maps-scraper)
  * [How it works](#how-it-works)
    + [Python code example](#python-code-example)
    + [Output Example](#output-example)
      
In this tutorial, we'll demonstrate how to extract data from Google Maps. In the first part of the tutorial, we'll use a free tool, built for smaller scale scraping. In the second part, we'll show how to use Oxylabs API for more effective, bigger scale scraping (you can get a free trial [here](https://dashboard.oxylabs.io/en/). 

## Free Google Maps Scraper

### Prerequisites

To run this tool, you need to have Python 3.11 installed in your system.

### Installation

Open up a terminal window, navigate to this repository and run this command:

`make install`

### Getting the URL for the Maps page to scrape

This tool is used to scrape Google Maps results from a given search results page.

First of all, open up Google Maps and enter something to search for in the `Search` field. 

We'll be searching for restaurants in Manhattan, New York.

<img width="1216" alt="image" src="https://github.com/user-attachments/assets/cb49cafb-9d06-41e2-9320-aad209ea8fdf">

After pressing enter, copy and save the URL of the page you landed on. We'll be using it in the scraping tool.

In this example, we'll be using this URL: `https://www.google.com/maps/search/restaurants/@40.7660158,-73.9833944,14z/data=!4m5!2m4!5m2!1e0!4e9!6e5?entry=ttu`

### Scraping 

To scrape Google Maps results from your provided URL, run this command in your terminal:
`make scrape URL='<url>'`

With the URL we retrieved before, the command should look like this:

`make scrape URL='https://www.google.com/maps/search/restaurants/@40.7660158,-73.9833944,14z/data=!4m5!2m4!5m2!1e0!4e9!6e5?entry=ttu'`

By default, the tool will scrape a small number of results that are visible when you load the page.

To scrape the full results, add `FULL=True` to your command.

The full command should look like this:

`make scrape URL='https://www.google.com/maps/search/restaurants/@40.7660158,-73.9833944,14z/data=!4m5!2m4!5m2!1e0!4e9!6e5?entry=ttu' FULL=True`

Be aware that this will take a bit longer, since the tool will automatically scroll to the bottom of the results list.

After running the command, you should see this in your terminal:

<img width="928" alt="image" src="https://github.com/user-attachments/assets/d94124ac-6601-4680-8436-1b9c00010450">

When the tool has finished running, you should see a file named `locations.csv` in the directory you were running the tool.

If you open the generated CSV file, the data should look something like this:

<img width="622" alt="image" src="https://github.com/user-attachments/assets/24928dd3-d610-4a7a-a5bb-6201522f4280">

### Notes

In case the code doesn't work or your project is of bigger scale, please refer to the second part of the tutorial. There, we showcase how to scrape public data with Oxylabs Scraper API.

## Oxylabs Google Maps Scraper

Google Maps Scraper enables effortless public data extraction with
geographic references from Google Maps and Google Places. This short
guide will show you the process of scraping Google Maps using Oxylabs'
Scraper API.

## How it works

You can retrieve Google Maps data by providing the URL to our service.
Our API will return the results in JSON format.

### Python code example

The below code examples demonstrate how you can get Google Maps results.
First, you need to send the instructions to our service using the
[<u>Push-Pull</u>](https://developers.oxylabs.io/scraper-apis/serp-scraper-api/integration-methods/push-pull)
method:

```python
import requests
from pprint import pprint

# Structure payload.
payload = {
    'source': 'google',
    'url': 'https://www.google.com/maps/search/restaurants/@40.7660158,-73.9833944,14z/data=!4m5!2m4!5m2!1e0!4e9!6e5?entry=ttu',
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

```

Once the job is done, you can retrieve the results by making another
request and including the **job ID** from the previous response, for
instance:

```python
import requests

# Get response.
response = requests.request(
    'GET',
    'http://data.oxylabs.io/v1/queries/{job_id}/results',
    auth=('USERNAME', 'PASSWORD')
)

# This will return the JSON response with results.
print(response.json())

```

### Output Example

The above code snippet will retrieve the results in JSON format:

```json
{
    "results": [
        {
            "content": "<!doctype html>\n<html lang=\"en\">\n<head>...</script></body>\n</html>\n",
            "created_at": "2023-07-25 10:01:01",
            "job_id": "7089545068712824833",
            "page": 1,
            "status_code": 200,
            "updated_at": "2023-07-25 10:01:20",
            "url": "https://www.google.com/maps/search/restaurants/@40.7660158,-73.9833944,14z/data=!4m5!2m4!5m2!1e0!4e9!6e5?entry=ttu"
        }
    ]
}
```

From local landmarks to various businesses, with Oxylabs’ Google Maps
Scraper you’ll easily access the public data you need. If you have any
questions or need assistance, don’t hesitate to contact our 24/7 support
team via live chat or [<u>email</u>](mailto:support@oxylabs.io).

Read More Google Scraping Related Repositories: [Google Sheets for Basic Web Scraping](https://github.com/oxylabs/web-scraping-google-sheets), [How to Scrape Google Shopping Results](https://github.com/oxylabs/scrape-google-shopping), [Google Play Scraper](https://github.com/oxylabs/google-play-scraper), [How To Scrape Google Jobs](https://github.com/oxylabs/how-to-scrape-google-jobs), [Google News Scrpaer](https://github.com/oxylabs/google-news-scraper), [How to Scrape Google Scholar](https://github.com/oxylabs/how-to-scrape-google-scholar), [How to Scrape Google Flights with Python](https://github.com/oxylabs/how-to-scrape-google-flights), [How To Scrape Google Images](https://github.com/oxylabs/how-to-scrape-google-images), [Scrape Google Search Results](https://github.com/oxylabs/scrape-google-python), [Scrape Google Trends](https://github.com/oxylabs/how-to-scrape-google-trends)

### Featured in Technical Communities
We’re excited to see that our content and tools are being referenced by developers and technical writers across platforms!

* [The 15 Best Web Scraping Tools to Explore in 2025](https://medium.com/@marvis.crisco67/the-15-best-web-scraping-tools-152d42198234)

* [10 Best Google Maps Scrapers In 2025](https://medium.com/@david.henry.124/best-google-maps-scrapers-ae2735cdc5fd)

* [How to Scrape Google Flights Data](https://medium.com/@marvis.crisco67/how-to-scrape-google-flights-data-4df30edb1d22)

**Contacts**

Email - hello@oxylabs.io 

Drop a message - <br><a href="https://oxylabs.drift.click/oxybot">Live chat</a>
