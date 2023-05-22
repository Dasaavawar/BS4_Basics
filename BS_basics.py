import requests
from bs4 import BeautifulSoup

url = 'https://www.your-website.com/'

website_doc = requests.get(url).text
soup = BeautifulSoup(website_doc, 'html.parser')

# <a href='link'>click</a>

links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

print(links)
print(len(links))