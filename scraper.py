'Sim'
# scraper.py
import requests
from bs4 import BeautifulSoup


def buscar_pagina(url):
    """Visita uma URL e retorna todo o seu conteúdo HTML como texto."""
    try:
        resposta = requests.get(url)
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
    titulos = soup.find_all('h3', class_='title=')
    for livros in titulos:
        print(livros.text.strip())
