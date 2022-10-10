def criar_tabela():
    import sqlite3
    conexao = sqlite3.connect("agenda.db")
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE agenda(
        nome text,
        telefone text)
    ''')
    cursor.close()
    conexao.close()


def inserir_dados_tabela():
    import sqlite3
    conexao = sqlite3.connect("agenda.db")
    cursor = conexao.cursor()

    cursor.execute('''
        insert into agenda(nome, telefone)
            values(?,?)
            ''', ("NILO", "7788-1432"))
    conexao.commit()
    cursor.close()
    conexao.close()


def consulta_dados_agenda():
    import sqlite3
    conexao = sqlite3.connect("agenda.db")
    cursor = conexao.cursor()

    cursor.execute("select * from agenda")
    resultado = cursor.fetchone()
    print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}\n")

    cursor.close()
    conexao.close()


def inserir_dados_com_lista():
    import sqlite3
    conexao = sqlite3.connect("agenda.db")
    cursor = conexao.cursor()

    dados = [("João", "98901-0109"),
             ("André", "98902-8900"),
             ("Maria", "97891-3321")]
    cursor.executemany('''
        insert into agenda (nome, telefone)
        values (?,?)
        ''', dados)
    conexao.commit()
    cursor.close()
    conexao.close()


def consulta_multiplos_dados():
    import sqlite3
    conexao = sqlite3.connect("agenda.db")
    cursor = conexao.cursor()

    cursor.execute("select * from agenda")
    resultado = cursor.fetchall()
    for registro in resultado:
        print(f"Nome:{registro[0]}\nTelefone: {registro[1]}\n")

    cursor.close()
    conexao.close()


def consulta_registro_por_registro():
    import sqlite3
    conexao = sqlite3.connect("agenda.db")
    cursor = conexao.cursor()

    cursor.execute("select * from agenda")
    while True:
        resultado = cursor.fetchone()
        if resultado is None:
            break
        print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}\n{'='* 20}")

    cursor.close()
    conexao.close()


def atualizar_registros():
    import sqlite3
    from contextlib import closing

    with sqlite3.connect("agenda.db") as conexao:
        with closing(conexao.cursor()) as cursor:
            cursor.execute(""" update agenda 
                                    set telefone = '12345-6789'
                                    where nome = 'NILO'""")
    conexao.commit()
