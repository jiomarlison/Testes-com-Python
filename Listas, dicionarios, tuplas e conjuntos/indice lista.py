numero = [0, 0, 0, 0, 0]
x = 0

while x < 5:
    numero[x] = int(input(f'Número {x + 1}: '))
    x += 1

while True:
    escolhido = int(input('Que posição você quer imprimir (0 para sair): '))
    if escolhido == 0:
        break
    elif escolhido > len(numero):
        print('\033[31mPosição não existente\033[m')
    else:
        print(f'Você escolheu o número: {numero[escolhido - 1]}')
