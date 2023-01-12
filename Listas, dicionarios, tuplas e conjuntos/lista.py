notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0

while x < len(notas):
    notas[x] = float(input(f'Digite a {x+1}º nota: '))
    soma += notas[x]
    x += 1

x = 0

while x < len(notas):
    print(f'Nota: {x}: {notas[x]:6.2f}')
    x += 1

print(f'Méia: {soma / x:5.2f}')

#%%
