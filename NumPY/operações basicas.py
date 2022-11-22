import numpy as np

#  a = np.arange(25).reshape(5, 5),
# 'a' recebe a biblioteca(np) para usar os metodos,os valores(.arange()) e formatação(.reshape())
# np.arange(25) conta de 0 até o numero que esta no parentese menos 1
# .reshape(5, 5) faz com que o arange de cima fique no formato de 5 linhas e 5 colunas
a = np.arange(25).reshape(5, 5)
print(f"A:{a}\n")

b = np.array([20, 30, 40, 50])
print(f"B:{b}\n")
c = np.arange(4)
print(f"C:{c}\n")

d = b - c
print(f"D = B - C\nD:{d}\n")

print(f"\nC**2:", c**2)

print("\n10 * np.sin(a):", 10 * np.sin(b))

print("\nB<35:", b < 35)
