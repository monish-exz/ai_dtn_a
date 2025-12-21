import requests
from bs4 import BeautifulSoup
from datetime import datetime


# Configuration: number of articles to scrape per website
ARTICLES_PER_SITE = 8


# This function collects AI news from multiple RSS feeds
def scrape_all_websites():
    news_data = []

    # Get today's date
    today = datetime.today().strftime("%Y-%m-%d")

    # List of RSS feeds to scrape
    rss_feeds = [
        {
            "name": "TechCrunch",
            "url": "https://techcrunch.com/tag/artificial-intelligence/feed/"
        },
        {
            "name": "MIT Technology Review",
            "url": "https://www.technologyreview.com/feed/"
        },
        {
            "name": "Analytics India Magazine",
            "url": "https://analyticsindiamag.com/feed/"
        },

    ]

    # Loop through each website
    for site in rss_feeds:
        try:
            # Request RSS feed data
            response = requests.get(site["url"], timeout=10)

            # Parse RSS XML content
            soup = BeautifulSoup(response.content, "xml")

            # Get limited number of articles
            items = soup.find_all("item")[:ARTICLES_PER_SITE]

            # Extract details from each article
            for item in items:
                title = item.title.text if item.title else "No title"
                link = item.link.text if item.link else ""

                # Extract and clean article summary
                summary = ""
                if item.description:
                    summary = BeautifulSoup(
                        item.description.text,
                        "html.parser"
                    ).get_text(strip=True)

                # Store article data
                news_data.append([
                    title,
                    today,
                    site["name"],
                    link,
                    summary
                ])

        except Exception as e:
            # Print error if RSS feed fails
            print(f"RSS error ({site['name']}): {e}")

    return news_data
