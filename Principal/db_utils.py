'db_livros'
# db para armazenar os livros

import sqlite3


def salvar_livros_db(lista_livros):
    'recebe e salva a lista dos livros'
    with sqlite3.connect('livros.db') as connection:
        cursor = connection.cursor()
        print('Your DB has been created and you can use it now!')

        # CRIANDO A TABELA
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS Livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT NOT NULL,
            Price REAL,
            UNIQUE(Title, Price)
            )
        '''

        # query = "DELETE FROM Livros WHERE id > ?"

        # Executar o comando SQL no DB
        cursor.execute(create_table_query)
        # cursor.execute(query, (20,))

        # Fazer o commit das changes
        connection.commit()

        # Mensagem confirmando que deu certo
        print("Table 'Livros' successfully created")
        print('Loading data...')
        valores = [(d['Título'], d['Preco']) for d in lista_livros]
        cursor.executemany("INSERT OR IGNORE INTO Livros (Title, Price)"
                           "VALUES (?, ?)", valores)
        connection.commit()
        print('DB updated.')
