'Sim'
# main.py
from scraper import buscar_todas_paginas, buscar_livros, buscar_pagina
from db_utils import salvar_livros_db  # Salva os livros no DB

if __name__ == "__main__":
    url_alvo = 'https://books.toscrape.com/catalogue/page-{}.html'
    # Um site simples para teste

    print(f"Buscando conteúdo da URL: {url_alvo}")
    lista_completa_de_livros = buscar_todas_paginas(url_alvo, num_paginas=50)

    if lista_completa_de_livros:
        print(f'\n ✓ Coleta finalizada! '
              f'Total de {len(lista_completa_de_livros)} livros encontrados.')
        salvar_livros_db(lista_completa_de_livros)
    else:
        print("Nenhum livro foi encontrado.")
