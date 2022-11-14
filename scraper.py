import requests
from bs4 import BeautifulSoup


# Scraping HTML from a single Sklearn docs page
def get_html(url):
    text = ''
    urls = []
    with open('urls.txt', 'r') as f:
        for line in f:
            urls.append(line)

    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        for data in soup(['style', 'script']):
            data.decompose()
        text += ' '.join(soup.stripped_strings).replace('\n', ' ')
    return text
