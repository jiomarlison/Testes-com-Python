import random

lista = []

for x in range(random.randint(10, 25)):
    lista.append(x)

print(lista)
print(lista[::2])
print(lista[1::2])
