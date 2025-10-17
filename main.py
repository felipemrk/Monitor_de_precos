'Sim'
# main.py
from scraper import buscar_pagina  # Importa a ferramenta do nosso módulo

if __name__ == "__main__":
    url_alvo = 'https://books.toscrape.com/'  # Um site simples para teste

    print(f"Buscando conteúdo da URL: {url_alvo}")
    html_da_pagina = buscar_pagina(url_alvo)

    if html_da_pagina:
        print("\nConexão bem-sucedida! Os primeiros 500 caracteres da página são:")
        # Imprime só o comecinho para não poluir a tela
        print(html_da_pagina[:500])
