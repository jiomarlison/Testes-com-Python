import random

alfabeto_minusculo = 'abcdefghijklmnopqrstuvwxyz'
alfabeto_maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
especiais = ' !@#$%&*()_+-=/.,?:;<>[{]}'

uniao = alfabeto_minusculo + alfabeto_maiusculo + numeros + especiais
tamanho_senha = 64

senha = "".join(random.sample(uniao, tamanho_senha))

print(senha)
