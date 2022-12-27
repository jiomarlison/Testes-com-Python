import cv2
import mediapipe as mp

# INICIALIZAR O OPENCV E O MEDIAPIPE
webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rosto = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    # LER AS INFORMAÇÕES DA WEBCAM
    verificador, frame = webcam.read()
    if not verificador:
        break

    # RECONHECER OS ROSTOS QUE ESTÃO PRESENTES
    lista_rostos = reconhecedor_rosto.process(frame)
    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            # DESENHA O ROSTO NA IMAGEM
            desenho.draw_detection(frame, rosto)
    cv2.imshow("ROSTOS NA WEBCAM", frame)

    # QUANDO APERTAR ESC
    if cv2.waitKey(5) == 27:
        break


webcam.release()
cv2.destroyAllWindows()
