def gerador_texto():
    import random

    alfabeto_minusculo = 'bcdfghjklmnpqrstvwxyz'
    alfabeto_maiusculo = 'BCDFGHJKLMNPQRSTVWXYZ'
    especiais = ' ÁáÀàÂâÃãÉéÈèÊêÍíÌìÎîÓóÒòÔôÕõÚúÙùÛûÇç'

    uniao = alfabeto_minusculo + alfabeto_maiusculo + especiais
    tamanho_texto = 50

    text = "".join(random.sample(uniao, tamanho_texto))
    return text


def ajustar_texto(novo_texto, maiusc=False):
    # FUNÇÃO PARA REMOVER ESSAS LETRAS Á À Â Ã É È Ê Í Ì Î Ó Ò Ô Õ Ú Ù Û Ç
    # PARA DEIXAR APENAS ESPAÇOS SIMPLES
    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZÁáÀàÂâÃãÉéÈèÊêÍíÌìÎîÓóÒòÔôÕõÚúÙùÛûÇç'
    print(f'ANTES: \033[31m {novo_texto}\033[m')
    if maiusc:
        novo_texto = str(novo_texto).upper()
    else:
        novo_texto = str(novo_texto)

    for _ in range(len(novo_texto)):
        letra = novo_texto[_]
        if letra not in alfabeto:
            novo_texto = novo_texto.replace(f'{letra}', " ")

    while "  " in novo_texto:
        novo_texto = novo_texto.replace("  ", " ")

    novo_texto = novo_texto.replace('Á', 'A').replace('À', 'A').replace('Â', 'A').replace('Ã', 'A') \
        .replace('É', 'E').replace('È', 'E').replace('Ê', 'E').replace('Í', 'I').replace('Ì', 'I') \
        .replace('Î', 'I').replace('Ó', 'O').replace('Ò', 'O').replace('Ô', 'O').replace('Õ', 'O') \
        .replace('Ú', 'U').replace('Ù', 'U').replace('Û', 'U').replace('Ç', 'C').replace('á', 'a') \
        .replace('à', 'a').replace('â', 'a').replace('ã', 'a').replace('é', 'e').replace('è', 'e') \
        .replace('ê', 'e').replace('í', 'i').replace('ì', 'i').replace('î', 'i').replace('ó', 'o') \
        .replace('ò', 'o').replace('ô', 'o').replace('õ', 'o').replace('ú', 'u').replace('ù', 'u') \
        .replace('û', 'u').replace('ç', 'c')

    print(f'DEPOIS: \033[32m{novo_texto}\033[m')
    return novo_texto


def menu():
    import time
    lista_opcoes = ['=*=*=\033[36mLISTA DE OPÇÕES\033[m=*=*=\n',
                    '\033[29m 0 - ENCERRAR\033[m\n',
                    '\033[32m 1 - ESCREVER UMA FRASE\033[m\n',
                    '\033[33m 2 - VER UM EXEMPLO\033[m',
                    ]
    while True:
        print(f'{lista_opcoes[0]}{lista_opcoes[1]}{lista_opcoes[2]}{lista_opcoes[3]}')
        opcao = int(input('\033[34mEscolha sua opção: \033[m'))
        match opcao:
            case 0:
                print('Saindo...')
                time.sleep(1)
                break
            case 1:
                texto = str(input('Digite seu texto: '))
                resposta = str(input('\033[35mCONVERTER TEXTO PARA MAIUSCULO [S/N]: \033[m')).upper()[0]
                if resposta == 'S':
                    ajustar_texto(texto, True)
                    print('\n')
                elif resposta == 'N':
                    ajustar_texto(texto)
                    print('\n')
                else:
                    print('Resposta Invalida!\n')
            case 2:
                resposta = str(input('\033[35mCONVERTER TEXTO PARA MAIUSCULO [S/N]: \033[m')).upper()[0]
                if resposta == 'S':
                    ajustar_texto(gerador_texto(), True)
                    print('\n')
                elif resposta == 'N':
                    ajustar_texto(gerador_texto())
                    print('\n')
                else:
                    print('Resposta Invalida!\n')
            case _:
                print('\033[31mOpção Invalida!\033[31m\n')


menu()
