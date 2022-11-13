import requests
from bs4 import BeautifulSoup


# Scraping HTML from a single Sklearn docs page
def get_html(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Get the main content of the page
    for data in soup(['style', 'script']):
        data.decompose()

    text = ' '.join(soup.stripped_strings).replace('\n', ' ')
    return text
