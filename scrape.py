import requests
from bs4 import BeautifulSoup

def scrape(url):
    response = requests.get(url)

    document = BeautifulSoup(response.text, 'html.parser')

    # Find elements with attribute data-lyrics-container="true"
    elements = document.find_all(attrs={'data-lyrics-container': 'true'})

    text = '\n'.join([e.get_text(separator='\n') for e in elements])

    filename = url.replace('https://genius.com/', '') + '.txt'
    with open(filename, 'w') as f:
        f.write(text)

urls = [
]
for url in urls:
    print('Scraping', url, '...')
    scrape(url)
