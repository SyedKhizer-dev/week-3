import logging

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def remove_html_tags(url: str) -> str:
    """Download a webpage and return its text without HTML tags."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException:
        logger.exception("Failed to download webpage: %s", url)
        raise

    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text(separator=" ", strip=True)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    webpage_url = input("Enter a URL: ").strip()

    try:
        print(remove_html_tags(webpage_url))
    except requests.RequestException:
        print("Could not download the webpage. Check the URL and your connection.")
