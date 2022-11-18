def criar_tabela_dados_registro():
    import sqlite3
    conexao = sqlite3.connect("dados_registro.db")
    cursor = conexao.cursor()

    try:
        cursor.execute('''
                create table if not exists dados_registro(
                matricula int primary key not null unique,
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
    import sqlite3
    conexao = sqlite3.connect("registro_ponto.db")
    cursor = conexao.cursor()

    try:
        cursor.execute('''
                create  table if not exists registro_ponto(
                matricula int primary key not null,
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
    import sqlite3
    conexao = sqlite3.connect("dados_registro.db")
    cursor = conexao.cursor()

    matricula = int(input("Digite a matricula: "))
    nome = str(input("Digite o nome: ").strip().upper())
    nascimento = str(input("Digite a data de nascimento(dia/mes/ano): "))
    funcao = str(input("Digite  a função: ").strip().upper())

    lista_dados = [matricula, nome, nascimento, funcao]

    cursor.execute(f"""insert into dados_registro(matricula, nome, nascimento, funcao) values (?,?,?,?)""", lista_dados)
    conexao.commit()

    print(f"Novo Membro, Nº matricula:{matricula}, Nome:{nome}, Nascimento:{nascimento}, Função:{funcao}, Inserido com Sucesso\n")
    cursor.close()
    conexao.close()


def consulta_dados_registro():
    import sqlite3
    conexao = sqlite3.connect("dados_registro.db")
    cursor = conexao.cursor()

    cursor.execute("select * from dados_registro order by matricula")
    resultado = cursor.fetchall()
    for registro in resultado:
        print(f"Matricula:{registro[0]}\nNome: {registro[1]}\nNascimento:{registro[2]}\nFunção:{registro[3]}\n")

    cursor.close()
    conexao.close()


def teste_validacao_matricula():
    import sqlite3
    conexao = sqlite3.connect("dados_registro.db")
    cursor = conexao.cursor()

    lista_matriculas = [] #ARMAZENA TODAS AS MATRICULAS DE dados_registro VALIDAS
    mat_pesquisa = int(input("digite uma matricula: ")) #VARIAVEL PARA PESQUISA DE UMA MATRIZ

    cursor.execute("select matricula from dados_registro") #SELECIONA TODAS AS MATRICULAS DO BANCO
    resultado = cursor.fetchall() #ARMAZENA TODAS AS MATRICULAS EM UMA LISTA
    for registro in resultado: #PERCORRE TODAS AS MATRICULAS EM resultado
         lista_matriculas.append(registro[0])  #ADICIONA AS MATRICULAS NA LISTA PARA VALIDAR

    if mat_pesquisa in lista_matriculas: #VAZ A VALIDAÇÃO SE A MATRICULA PESQUISADA EXISTE NA LISTA DE MATRICULAS VALIDAS
        cursor.execute(f"select * from dados_registro where matricula = {mat_pesquisa} order by matricula") #PESQUISA TODOS OS DADOS EM dados_registro DA MATRICULA PESQUISADA
        resultado = cursor.fetchall() # ARMAZENA OS RESULTADOS DA PESQUISA
        for dados in resultado:
            print(f"Matricula: {dados[0]}, Nome: {dados[1]}, Nascimento: {dados[2]}, Função: {dados[3]}\n") #MOSTRA OS DADOS DA MATRICULA PESQUISADA
    else: #CASO NÃO SEJA UMA MATRICULA VALIDA RETORNA UMA MENSAGEM
        print("não esta")

    cursor.close()
    conexao.close()


def consulta_registro_ponto():
    import sqlite3
    conexao = sqlite3.connect("registro_ponto.db")
    cursor = conexao.cursor()

    cursor.execute("select * from registro_ponto order by matricula")
    resultado = cursor.fetchall()
    for registro in resultado:
        print(f"Matricula:{registro[0]}\nDia: {registro[1]}\nEntrada1:{registro[2]}\n")

    cursor.close()
    conexao.close()


def consulta_registro_ponto_hoje():
    import datetime as dt
    import sqlite3

    agora = dt.datetime.now()
    data_hoje = agora.strftime("%d/%m/%Y")
    conexao = sqlite3.connect("registro_ponto.db")
    cursor = conexao.cursor()

    cursor.execute(f"select * from registro_ponto where dia like '{data_hoje}' order by matricula")
    resultado = cursor.fetchall()
    for registro in resultado:
        print(f"Matricula:{registro[0]};Dia: {registro[1]};Entrada1:{registro[2]}\n")

    cursor.close()
    conexao.close()

def inserir_entrada_1_em_registro_ponto():
    import datetime as dt
    import sqlite3

    conexao = sqlite3.connect("registro_ponto.db")
    cursor = conexao.cursor()

    matricula = int(input("Digite a matricula: "))
    agora = dt.datetime.now()
    data_hoje = agora.strftime("%d/%m/%Y")
    hora_agora = agora.strftime("%H:%M:%S")


    lista_dados = [matricula, data_hoje, hora_agora]

    cursor.execute(f"""insert into registro_ponto(matricula, dia, entrada_1) values (?,?,?)""", lista_dados)
    conexao.commit()

    cursor.close()
    conexao.close()


print("registros hoje")
consulta_registro_ponto_hoje()
print("registros gerais")
consulta_registro_ponto()