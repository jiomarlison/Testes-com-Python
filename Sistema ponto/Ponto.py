import sqlite3
import datetime as dt


def criar_tabela_dados_registro():
    conexao = sqlite3.connect("ponto.db")
    cursor = conexao.cursor()

    try:
        cursor.execute('''
                create table if not exists dados_registro(
                matricula int primary key,
                nome text not null,
                nascimento text not null,
                funcao text not null
                                                            );
                            ''')
        print("Tabela dados_registro criada com sucesso")
    except:
        print("Não foi possivel criar a tabela dados_registro")

    cursor.close()
    conexao.close()


def criar_tabela_registro_de_ponto():
    conexao = sqlite3.connect("ponto.db")
    cursor = conexao.cursor()

    try:
        cursor.execute('''
                create  table if not exists registro_ponto(
                n_matricula int not null,
                dia text not null,
                entrada_1 text,
                saida_1 text,
                entrada_2 text,
                saida_2 text,
                foreign key (matricula) references dados_registro(matricula)
                                                              );
                                                              ''')
        print("Tabela registro_ponto criada com sucesso")
    except:
        print("Não foi possivel criar a registro_de_ponto")

    cursor.close()
    conexao.close()


def inserir_novo_membro():
    conexao = sqlite3.connect("ponto.db")
    cursor = conexao.cursor()

    matricula = int(input("Digite a matricula: "))

    cursor.execute(f"""select n_matricula from dados_registro where n_matricula = {matricula}""")
    resposta = str(cursor.fetchall()).replace('[', '').replace(']', '').replace('(', '').replace(')', '')

    if resposta == '':
        nome = str(input("Digite o nome: ").strip().upper())
        nascimento = str(input("Digite a data de nascimento(dia/mes/ano): "))
        funcao = str(input("Digite  a função: ").strip().upper())

        lista_dados = [matricula, nome, nascimento, funcao]

        cursor.execute(f"""insert into dados_registro(n_matricula, nome, nascimento, funcao) values (?,?,?,?)""", lista_dados)
        conexao.commit()

        print(f"Novo Membro, Nº matricula:{matricula}, Nome:{nome}, Nascimento:{nascimento}, Função:{funcao}, Inserido com Sucesso\n")


    else:
        print('Já existe alguém com esse numero de matricula')
        cursor.execute(f'select * from dados_registro where n_matricula = {matricula}')
        registro = cursor.fetchall()
        for resultado in registro:
            print(f'Matricula: {resultado[0]}, Nome: {resultado[1]}, Nascimento: {resultado[2]}, Função: {resultado[3]}')

    cursor.close()
    conexao.close()


def inserir_entrada_1_em_registro_ponto():
    conexao = sqlite3.connect("ponto.db")
    cursor = conexao.cursor()

    print('REGISTRAR ENTRADA')

    matricula = int(input("Digite a matricula: "))
    agora = dt.datetime.now()
    data_hoje = agora.strftime("%d/%m/%Y")
    hora_agora = agora.strftime("%H:%M:%S")

    lista_dados = [matricula, data_hoje, hora_agora]

    cursor.execute(f"select entrada_1 from registro_ponto where n_matricula = {matricula} and dia = '{data_hoje}")
    entrada_1 = str(cursor.fetchall()).replace('[', '').replace(']', '').replace('(', '').replace(')', '')

    if entrada_1 != 'None,':
        print('Entrada já registrada')
    else:
        cursor.execute(f"""insert into registro_ponto(n_matricula, dia, entrada_1) values (?,?,?)""", lista_dados)
        conexao.commit()

    cursor.close()
    conexao.close()


def inserir_saida_1_em_registro_ponto():
    conexao = sqlite3.connect("ponto.db")
    cursor = conexao.cursor()

    print('REGISTRAR INICIO INTERVALO')

    matricula = int(input("Digite a matricula: "))
    agora = dt.datetime.now()
    data_hoje = agora.strftime("%d/%m/%Y")
    hora_agora = agora.strftime("%H:%M:%S")

    cursor.execute(f"select entrada_1 from registro_ponto where n_matricula = {matricula}  and dia = '{data_hoje}")
    entrada_1 = str(cursor.fetchall()).replace('[', '').replace(']', '').replace('(', '').replace(')', '')

    cursor.execute(f"select saida_1 from registro_ponto where n_matricula = {matricula} and dia = '{data_hoje}")
    saida_1 = str(cursor.fetchall()).replace('[', '').replace(']', '').replace('(', '').replace(')', '')

    print(f'Matricula: {matricula} Entrada: {entrada_1} intervalo: {saida_1}')

    if entrada_1 == 'None,':
        print('Está pessoa não tem um registro de entrada')
        print('deseja registra sua entrada (S/N)?')
        resposta = str(input('Digite sua resposta: ')).strip().upper()
        if resposta == 'S':
            cursor.execute(
                f"""UPDATE registro_ponto SET entrada_1 = '{hora_agora}' WHERE n_matricula = {matricula} and dia = '{data_hoje}'""")
            conexao.commit()
        else:
            print('Saindo')
    elif saida_1 != 'None,':
        print('Intervalo Já registrado!')
    else:
        cursor.execute(f"""UPDATE registro_ponto SET saida_1 = '{hora_agora}' WHERE n_matricula = {matricula} and dia = '{data_hoje}'""")
        conexao.commit()
        print('intervalo registrado com sucesso!')
        cursor.execute(f"select n_matricula, dia, entrada_1, saida_1 from registro_ponto where dia like '{data_hoje}' and n_matricula = {matricula} order by matricula")
        resultado = cursor.fetchall()
        print(resultado)

    cursor.close()
    conexao.close()


def consulta_dados_registro():
    conexao = sqlite3.connect("ponto.db")
    cursor = conexao.cursor()

    cursor.execute("select * from dados_registro order by n_matricula")
    resultado = cursor.fetchall()
    print('\033[32m DADOS MEMBROS CADASTRADOS \033[m')
    for registro in resultado:
        print(f"Matricula:{registro[0]}\nNome: {registro[1]}\nNascimento:{registro[2]}\nFunção:{registro[3]}\n")

    cursor.close()
    conexao.close()


def consulta_registro_ponto():
    conexao = sqlite3.connect("ponto.db")
    cursor = conexao.cursor()

    cursor.execute("select * from registro_ponto order by n_matricula")
    resultado = cursor.fetchall()
    for registro in resultado:
        print(f"Matricula:{registro[0]}\nDia: {registro[1]}\nEntrada1:{registro[2]}\n")

    cursor.close()
    conexao.close()


def consulta_registro_ponto_hoje():

    agora = dt.datetime.now()
    data_hoje = agora.strftime("%d/%m/%Y")
    conexao = sqlite3.connect("ponto.db")
    cursor = conexao.cursor()

    cursor.execute(f"""
        select
    registro_ponto.n_matricula,
    dados_registro.nome,
    registro_ponto.dia,
    registro_ponto.entrada_1,
    registro_ponto.saida_1,
    registro_ponto.entrada_2,
    registro_ponto.saida_2
        from registro_ponto
        join dados_registro on dados_registro.matricula = registro_ponto.n_matricula
        where dia like '{data_hoje}' 
        order by n_matricula
                    """)
    resultado = cursor.fetchall()
    for registro in resultado:
        print(f"\nMatricula: {registro[0]};\nNome: {registro[1]};\nDia: {registro[2]};\nEntrada: {registro[3]};\nInicio Intervalo: {registro[4]};\nFim Intervalo: {registro[5]};\n;\nSaida: {registro[6]};\n")

    cursor.close()
    conexao.close()

