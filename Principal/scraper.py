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
        price = float(price[1:])
        dicio = {'Título': titulo, 'Preco': price}
        lista_dicio_livros.append(dicio)
    return lista_dicio_livros


def buscar_generos(html):
    'Encontra todos os gêneros para realizar a procura dos livros'
    lista_generos = []
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup.find_all('ul', class_="nav nav-list"):
        genre = tag.find('ul').find('a', href=True).text
        link = tag.find('ul').find('a', href=True).get('href')
        dicio_generos = {"Genero": genre.strip(), "Link": link}
        lista_generos.append(dicio_generos)
    return lista_generos


# Adicionado pelo Claude
def buscar_todas_paginas(url_base, num_paginas=50):
    """
    Busca livros de múltiplas páginas.

    Args:
        url_base: URL com placeholder {} para o número da página
        num_paginas: Quantidade de páginas para buscar (padrão: 5)

    Returns:
        Lista com todos os livros encontrados
    """
    lista_completa_de_livros = []

    for i in range(1, num_paginas + 1):
        url_da_pagina_atual = url_base.format(i)
        print(f"Buscando dados da página {i}...")

        html_da_pagina = buscar_pagina(url_da_pagina_atual)

        if html_da_pagina:
            livros_desta_pagina = buscar_livros(html_da_pagina)
            lista_completa_de_livros.extend(livros_desta_pagina)
        else:
            print(f"⚠ Não foi possível acessar a página {i}")

    return lista_completa_de_livros


# Ver amanhã como buscar os dois.
# Pensei em adicionar os dois em listas e depois adiciona-los ao dicio

print(buscar_generos(buscar_pagina('https://books.toscrape.com/')))
