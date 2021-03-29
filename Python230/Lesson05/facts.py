import requests
from bs4 import BeautifulSoup

response = requests.get('http://unkno.com/')

soup = BeautifulSoup(response.content, 'html.parser')
fact = soup.find_all('div', id = 'content')

print(fact[0].getText())
