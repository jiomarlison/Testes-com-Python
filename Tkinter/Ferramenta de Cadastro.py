import tkinter as tk
from tkinter import ttk
import datetime as dt

OPCOES = ["Entrada", "Início Intervalo", "Fim Intervalo", "Saída"]
agora = dt.datetime.now()
agora = agora.strftime("%d/%m/%Y - %H:%M:%S")

# TITULO E CONFIGURAÇÕES DA JANELA
janela = tk.Tk()
janela.title('Cadastro de Matricula')
janela.minsize(100, 100)
janela.maxsize(300, 400)


def dados_do_ponto():
    matricula = entry_matricula.get()
    data_e_hora = dt.datetime.now()
    dia = data_e_hora.strftime("%d/%m/%Y")
    hora = data_e_hora.strftime("%H:%M:%S")
    tipo = entrada_ou_saida.get()
    lista_dados = [matricula, dia, hora, tipo]
    print(lista_dados)
    inserir = open('REGISTRO DE PONTO.txt', 'at', encoding='utf-8')
    inserir.write(f'NÚMERO DA MÁTRICULA: {matricula}, DESCRIÇÃO: {tipo}, DATA: {dia}, HORA: {hora} \n')

    data_agora = tk.Label(janela, text=f'Data atual: {agora}', font="Arial")


label_descricao = tk.Label(text="Número da Matricula", font="Arial")
label_descricao.grid(column=0, row=0, padx=5, pady=5, columnspan=4, sticky='nswe')

entry_matricula = tk.Entry()
entry_matricula.grid(column=0, row=1, padx=5, pady=5, columnspan=1, sticky='nswe')

data_agora = tk.Label(janela, text=f'Data atual: {agora}', font="Arial")
data_agora.grid(column=0, row=2, padx=5, pady=5, columnspan=1, sticky='nswe')

entrada_ou_saida = ttk.Combobox(values=OPCOES, state='readonly')
entrada_ou_saida.current(0)
entrada_ou_saida.grid(column=0, row=3, padx=5, pady=5, columnspan=4, sticky='nswe')

botao_registro = tk.Button(text="Marcar Ponto", command=dados_do_ponto)
botao_registro.grid(column=0, row=4, padx=5, pady=5, columnspan=4, sticky='nswe')

janela.mainloop()
