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


def consulta_dados_agenda():
    import sqlite3
    conexao = sqlite3.connect("dados_registro.db")
    cursor = conexao.cursor()

    cursor.execute("select * from dados_registro")
    resultado = cursor.fetchall()
    for registro in resultado:
        print(f"Matricula:{registro[0]}\nNome: {registro[1]}\nNascimento:{registro[2]}\nFunção:{registro[3]}\n")

    cursor.close()
    conexao.close()


inserir_novo_membro()
consulta_dados_agenda()
