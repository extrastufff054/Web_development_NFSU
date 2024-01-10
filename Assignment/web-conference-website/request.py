import requests
from bs4 import BeautifulSoup

url = "https://www.conferences2023.nfsu.semintelligence.org/home"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

with open('webpage.html','w', encoding = 'utf-8') as f :
    f.write(str(soup))


