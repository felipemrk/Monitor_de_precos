'db'
import sqlite3

with sqlite3.connect('user.db') as connection:
    cursor = connection.cursor()
    print('Success! Database created and ready to use!')

    # CRIANDO A TABELA
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        email TEXT
    );
    '''

    # Executando o comando SQL (agora aparece como func ali em cima)
    cursor.execute(create_table_query)

    # Commitando as changes
    connection.commit()

    # Mensagem de confirmação
    print("Table 'Students' created successfully!")
