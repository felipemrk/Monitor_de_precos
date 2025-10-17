'Sim'
# main.py
from scraper import buscar_pagina  # Importa a ferramenta do nosso módulo
from scraper import buscar_livros  # Importa o buscador de livros

if __name__ == "__main__":
    url_alvo = 'https://books.toscrape.com/'  # Um site simples para teste

    print(f"Buscando conteúdo da URL: {url_alvo}")
    html_da_pagina = buscar_pagina(url_alvo)

    if html_da_pagina:
        print("\nConexão bem-sucedida!")
        # Imprime só o comecinho para não poluir a tela
        buscar_livros(html_da_pagina)
