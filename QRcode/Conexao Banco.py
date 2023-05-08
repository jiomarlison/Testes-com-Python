import sqlite3
from contextlib import closing
with sqlite3.connect('FRUIT_FLOW_DATABASE.db') as conexao:
    with closing(conexao.cursor()) as cursor:
        # cursor.execute('''CREATE TABLE REGISTRO(CODIGO int, PESO float)''')
        # cursor.execute('''delete from REGISTRO where CODIGO = 111122223333''')
        # conexao.commit()
        cursor.execute('''select * from registro''')

        resultado = cursor.fetchall()
        if resultado is None:
            print('Nada registrado')
        else:
            for registro in resultado:
                print(f'BANCO DE DADOS - Codigo: {registro[0]}, Peso: {registro[1]:5.3f}')

