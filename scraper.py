'Sim'
# scraper.py
import requests
from bs4 import BeautifulSoup


def buscar_pagina(url):
    """Visita uma URL e retorna todo o seu conteúdo HTML como texto."""
    try:
        resposta = requests.get(url)
        resposta.encoding = 'utf-8'
        # Verifica se a requisição foi bem-sucedida (código 200)
        if resposta.status_code == 200:
            return resposta.text
        else:
            print(f"Erro ao acessar a página. Código: {resposta.status_code}")
            return None
    except Exception as e:
        print(f"Ocorreu um erro na requisição: {e}")
        return None


def buscar_livros(html):
    'Encontrar o título dos livros'
    soup = BeautifulSoup(html, 'html.parser')
    lista_dicio_livros = []
    for tag in soup.find_all('article', class_="product_pod"):
        titulo = tag.find('h3').find('a').get('title')
        price = tag.find('p', class_='price_color').text
        dicio = {'Título': titulo, 'Preco': price}
        lista_dicio_livros.append(dicio)
    return lista_dicio_livros

# Ver amanhã como buscar os dois.
# Pensei em adicionar os dois em listas e depois adiciona-los ao dicio
