import sqlite3
conexao = sqlite3.connect("agenda.db")
cursor = conexao.cursor()


def criar_tabela():
    cursor.execute('''
        CREATE TABLE agenda(
        nome text,
        telefone text)
    ''')


def inserir_dados_tabela():
    cursor.execute('''
        insert into agenda(nome, telefone)
            values(?,?)
            ''', ("NILO", "7788-1432"))


def consulta_dados_agenda():
    cursor.execute("select * from agenda")
    resultado = cursor.fetchone()
    print(f"Nome: {resultado[0]}\nTelefone: {resultado[1]}\n")


def inserir_dados_com_lista():
    dados = [("João", "98901-0109"),
             ("André", "98902-8900"),
             ("Maria", "97891-3321")]
    cursor.executemany('''
        insert into agenda (nome, telefone)
        values (?,?)
        ''', dados)


def consulta_multiplos_dados():
    cursor.execute("select * from agenda")
    resultado = cursor.fetchall()
    for registro in resultado:
        print(f"Nome:{registro[0]}\nTelefone: {registro[1]}\n")


consulta_multiplos_dados()

conexao.commit()
cursor.close()
conexao.close()
