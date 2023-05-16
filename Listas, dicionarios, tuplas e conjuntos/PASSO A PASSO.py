import random

lista = []

for x in range(random.randint(1, 15)):
    lista.append(x)

print(lista)
print(lista[::2])
print(lista[1::2])
