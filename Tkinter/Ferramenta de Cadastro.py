import tkinter as tk
from tkinter import ttk
import datetime as dt

OPCOES = ["ENTRADA", "SAIDA"]
agora = dt.datetime.now()
agora = agora.strftime("%d/%m/%Y - %H:%M:%S")

# TITULO E CONFIGURAÇÕES DA JANELA
janela = tk.Tk()
janela.title('Cadastro de Matricula')
janela.minsize(300, 400)
janela.maxsize(300, 400)


def dados_do_ponto():
    matricula = entry_matricula.get()
    data_e_hora = dt.datetime.now()
    data_e_hora = data_e_hora.strftime("%d/%m/%Y - %H:%M:%S")
    tipo = entrada_ou_saida.get()
    lista_dados = [matricula, data_e_hora, tipo]
    print(lista_dados)


label_descricao = tk.Label(text="Número da Matricula", font="Arial")
label_descricao.grid(column=0, row=0, padx=5, pady=5, columnspan=4, sticky='nswe')

entry_matricula = tk.Entry()
entry_matricula.grid(column=0, row=1, padx=5, pady=5, columnspan=1, sticky='nswe')

data_agora = tk.Label(text=f'Data atual: {agora}', font="Arial")
data_agora.grid(column=0, row=2, padx=5, pady=5, columnspan=1, sticky='nswe')

entrada_ou_saida = ttk.Combobox(values=OPCOES)
entrada_ou_saida.grid(column=0, row=3, padx=5, pady=5, columnspan=4, sticky='nswe')

botao_registro = tk.Button(text="Marcar Ponto", command=dados_do_ponto)
botao_registro.grid(column=0, row=4, padx=5, pady=5, columnspan=4, sticky='nswe')

janela.mainloop()
