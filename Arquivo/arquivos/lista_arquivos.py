import os
from Arquivo.lib.menu import *

lista_arquivos = os.listdir()
c = 1

print(f'\033[33m0\033[m - \033[34mSair\033[m')

for arquivos in lista_arquivos:
    if arquivos.endswith('.txt'):
        print(f'\033[33m{c}\033[m - \033[34m{arquivos}\033[m')
        c += 1

opcao = int(input('Digite o número do arquivo a selecionar: '))
if opcao > len(lista_arquivos) or opcao < 0:
    print('Digite um número de arquivo valido')
elif opcao == 0:
    print("\033[31mSaindo da lista")
else:
    print(lista_arquivos[opcao])
