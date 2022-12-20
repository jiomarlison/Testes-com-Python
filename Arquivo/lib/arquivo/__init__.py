from Arquivo.lib.menu import *
from datetime import *


def arqExist(nome):
    try:
        abrir = open(nome, 'rt')
        abrir.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome_arquivo):
    try:
        criar = open(f'C://Users//Secretaria//PycharmProjects//Testes-com-Python//Arquivo//arquivos//{nome_arquivo}',
                     'wt+')
        criar.close()
    except:
        print('\033[31mERRO!\033[m: Não foi possivel criar o arquivo!\033[m')
    else:
        print(f'Arquivo {nome_arquivo} criado com sucesso!')


def lerArquivo(nome_arquivo):
    try:
        ler = open(nome_arquivo, 'rt')
    except:
        print('\033[31mERRO!\033[m: Não foi possivel ler o arquivo')
    else:
        cabecalho('INFORMAÇÕES CADASTRADAS')
        for linha in ler:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', ' ')
            print(f'{dado[0]:<20}{dado[1]:>5}{dado[2]:>10}')
    finally:
        ler.close()


def cadastrar(nome_arquivo, nome='desconhecido', matricula=0):
    agora = datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    try:
        inserir = open(nome_arquivo, 'at')
    except:
        print('\033[31mERRO!\033[m: Não foi possivel abrir o arquivo!')
    else:
        try:
            inserir.write(f'Nome: {nome}; Matricula: {matricula}; Data de Registro: {agora} \n')
        except:
            print('\033[31mERRO!\033[m: Não foi possivel inserir a informação!')
        else:
            print(f'Novo registro de {nome} adicionado!')
            inserir.close()
