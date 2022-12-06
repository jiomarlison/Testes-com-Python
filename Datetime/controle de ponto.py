from datetime import *

matricula = input(int())
agora = datetime.now()
datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
ent1 = agora + timedelta(hours=0)
saida1 = ent1 + timedelta(hours=2)
ent2 = saida1 + timedelta(hours=2)
saida2 = ent2 + timedelta(hours=2)
soma_hora = saida1 - ent1 + saida2 - ent2
print(matricula, agora, ent1, saida1, ent2, saida2, soma_hora)



with open('texto.txt', 'a+') as arquivo:
    texto_aquivo = arquivo.write(f'''
Matricula: {matricula}
Agora: {datetime.now().strftime("%d/%m/%Y-%H:%M:%S")}
Entrada 1: {ent1.strftime("%d/%m/%Y-%H:%M:%S")}
Saida 1: {saida1.strftime("%d/%m/%Y-%H:%M:%S")}
Entrada 2 : {ent2.strftime("%d/%m/%Y-%H:%M:%S")}
Saida 2 : {saida2.strftime("%d/%m/%Y-%H:%M:%S")}
Soma de Horas: {soma_hora};
                                        ''')

with open('texto.txt', 'r') as arquivo:
    texto_aquivo = arquivo.readlines()
for linha in texto_aquivo:
    print(linha.replace("\n", ""))
