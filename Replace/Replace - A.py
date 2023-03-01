texto = str(input('Digite seu texto: ')).upper().rstrip().lstrip()

alfabeto_minusculo = 'abcdefghijklmnopqrstuvwxyz'
alfabeto_maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
especiais = '!?.,@#/'

# Á À Â Ã É È Ê Í Ì Î Ó Ò Ô Õ Ú Ù Û Ç

def ajustar_texto(novo_texto):
    novo_texto = str(novo_texto)
    # FUNÇÃO PARA REMOVER ESSAS LETRAS Á À Â Ã É È Ê Í Ì Î Ó Ò Ô Õ Ú Ù Û Ç
    # E PARA DEIXAR APENAS ESPAÇÕS SIMPLES
    alfabeto = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÂÃÉÈÊÍÌÎÓÒÔÕÚÙÛÇ'
    print(f'ANTES: {novo_texto}')

    for _ in range(len(novo_texto)):
        letra = novo_texto[_]
        if letra not in alfabeto:
            novo_texto = novo_texto.replace(f'{letra}', " ")

    while "  " in novo_texto:
        novo_texto = novo_texto.replace("  ", " ")
    novo_texto = novo_texto.replace('Á', 'A').replace('À', 'A').replace('Â', 'A').replace('Ã', 'A') \
        .replace('É', 'E').replace('È', 'E').replace('Ê', 'E').replace('Í', 'I').replace('Ì', 'I') \
        .replace('Î', 'I').replace('Ó', 'O').replace('Ò', 'O').replace('Ô', 'O').replace('Õ', 'A') \
        .replace('Ú', 'U').replace('Ù', 'U').replace('Û', 'U').replace('Ç', 'C')
    return novo_texto


print(f'DEPOIS: {ajustar_texto(texto)}')
