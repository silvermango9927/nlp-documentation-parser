import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    for data in soup([['style', 'script']]):
        data.decompose()

    text= ' '.join(soup.stripped_strings).replace('\n', ' ')
    return text
