import requests
from bs4 import BeautifulSoup

url = 'https://id.wikipedia.org/wiki/Halaman_Utama'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

object = soup.find(class_="mp-main-content")
items = object.find_all(class_="mp-content-box")
result = items[0]
print(result.encode('utf-8'))