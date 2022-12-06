def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número inteiro valido. \033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mUsuario Preferiu Não Digitar um Número. \033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '\033[32m=\033[m' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 0
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[36mSua opção: \033[m')
    return opc
