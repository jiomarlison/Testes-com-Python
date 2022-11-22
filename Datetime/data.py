from datetime import *
import math

lista = []

agora = date.today()
print(f"Data de hoje: {agora.strftime('%d/%m/%Y')}\n")

hora_agora = datetime.now()
hora_agora = time(hora_agora.hour, hora_agora.minute, hora_agora.second)
print(f'Hora agora: {hora_agora}\n')

inicio_ano = date(agora.year, 1, 1)
print(f'Começo do ano: {inicio_ano.strftime("%d/%m/%Y")}\n')

fim_do_ano = date(agora.year, 12, 31)
print(f'Fim do ano: {fim_do_ano.strftime("%d/%m/%Y")}\n')

n_dia = abs(agora-inicio_ano).days
print(f"Nº desse dia: {n_dia}\n")

n_semana = math.ceil(abs(agora-inicio_ano).days/7)
print(f"Nº da semana atual: {n_semana}\n")

n_para_fim_ano = abs(fim_do_ano - agora).days
print(f"Quantidade de dias para o fim do ano: {n_para_fim_ano}\n")

lista = [inicio_ano.strftime("%d/%m/%Y"), fim_do_ano.strftime("%d/%m/%Y"), n_para_fim_ano, agora.strftime("%d/%m/%Y"), hora_agora.strftime("%H:%M:%S"), n_dia, n_semana]
print(lista)