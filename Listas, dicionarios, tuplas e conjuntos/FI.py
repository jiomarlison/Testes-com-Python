n = int(input("Que termo deseja encontrar: "))
ultimo = 1
penultimo = 1

lista = []
termina02 = []

if (n == 1) or (n == 2):
    print("1")
else:
    count = 3
    lista = ['1', '1']
    for count in range(n-2):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        lista.append(f'{termo}')
        if '02' in f'{termo}':
            x = str(termo)
            if x[-2:] == '02':
                termina02.append(termo)


ultimo_text = str(lista[-1])
if ultimo_text[-2:] == '02':
    print(2)
else:
    print(f'\n{n}º elemento: {ultimo_text}\nDois ultimos digitos: {ultimo_text[-2]} e {ultimo_text[-1]}')
print(f'Numeros até {n} que terminam em 02: {termina02}')