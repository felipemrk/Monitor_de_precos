import requests
from bs4 import BeautifulSoup

# Fazendo a requisição para a página de notícias
url = 'https://books.toscrape.com/'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

# Criando o objeto Beautiful Soup
soup = BeautifulSoup(html, 'html.parser')

# Buscando todos os elementos que contêm os títulos das notícias
titulos = soup.find_all('p', class_='price_color')

# Extraindo e imprimindo os títulos
for tag_p in soup.find_all('p', class_='price_color'):
    print(tag_p.text)
