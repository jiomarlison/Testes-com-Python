import time

import cv2
import numpy as np
from pyzbar.pyzbar import decode

captura = cv2.VideoCapture(0)

while True:
    sucess, img = captura.read()

    if not sucess:
        break

    for code in decode(img):
        imagem_decodificada = code.data.decode("utf-8")
        rect_pts = code.rect

        if imagem_decodificada:
            pts = np.array([code.polygon], np.int32)
            cv2.polylines(img, [pts], True, (255, 0, 0), 3)
            cv2.putText(img, str(imagem_decodificada), (rect_pts[0], rect_pts[1]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 255, 0), 2)

    cv2.imshow('Imagem', img)
    cv2.waitKey(1)

captura.release()