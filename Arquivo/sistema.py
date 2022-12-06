from Arquivo.lib.menu import *
from Arquivo.lib.arquivo import *
from time import sleep

arquivo = 'sistema arquivo.txt'
LISTA_OPCOES = ['SAIR DO SISTEMA', 'CRIAR ARQUIVO', 'LER ARQUIVO', 'DELETAR ARQUIVO', 'INSERIR INFORMAÇÃO']

if arqExist(arquivo):
    print('Arquivo encontrado com sucesso')
else:
    print('arquivo não encontrado')
    criarArquivo(arquivo)

while True:
    resposta = menu(LISTA_OPCOES)
    if resposta == 0:
        print('\033[31mSaindo do sistema')
        break
    elif resposta == 1:
        print('\033[31m-->>\033[m', LISTA_OPCOES[1])
    elif resposta == 2:
        # Ler informações do arquivo!
        lerArquivo(arquivo)
    elif resposta == 3:
        print('\033[31m-->>\033[m', LISTA_OPCOES[3])
    elif resposta == 4:
        cabecalho('NOVA INFORMAÇÃO')
        nome = str(input('Digite o Nome: '))
        matricula = leiaInt('Matricula: ')
        cadastrar(arquivo, nome, matricula)
    else:
        print('\033[31mERRO! Digite uma opção valida!\033[m')
        sleep(1)
