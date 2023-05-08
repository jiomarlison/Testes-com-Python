import random
import time
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import sqlite3
from contextlib import closing

captura = cv2.VideoCapture(0)

while True:
    sucess, img = captura.read()
    if not sucess:
        print('Não foi possível abrir a camera!')
        break

    for code in decode(img):

        imagem_decodificada = code.data.decode("utf-8")

        if imagem_decodificada:
            peso = random.uniform(0.790, 0.900) + 0.000
            print(f'Código: {imagem_decodificada}, Peso: {peso:5.3f}')
            if float(0.800) <= peso <= float(0.850):
                with sqlite3.connect('FRUIT_FLOW_DATABASE.db') as conexao:
                    with closing(conexao.cursor()) as cursor:
                        cursor.execute('''insert into registro(CODIGO, PESO) values (?, ?)''', (imagem_decodificada, peso))
                        conexao.commit()
                        cursor.execute('''select * from registro''')
                        resultado = cursor.fetchall()
                        for registro in resultado:
                            print(f'BANCO DE DADOS - Codigo: {registro[0]}, Peso: {registro[1]:5.3f}')


    cv2.imshow('Imagem', img)
    cv2.waitKey(1)

captura.release()