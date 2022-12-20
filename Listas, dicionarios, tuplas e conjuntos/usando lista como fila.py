ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f'\nExistem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente ao fim da fila,')
    print('ou A para realizar um atendimento. S para sair.')

    operacao = str(input('Operações (F, A ou S): ')).upper()

    if operacao == 'A':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f'Cliente {atendido} atendido')
        else:
            print('Fila vazia! Ninguem para atender')
    elif operacao == 'F':
        ultimo += 1 #INCREMENTA O NOVO CLIENTE A SER ATENDIDO
        fila.append(ultimo)
    elif operacao == 'S':
        break
    else:
        print('Operação invalida! Digite apenas F, A ou S!')