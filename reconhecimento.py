import cv2
from ultralytics import YOLO

def iniciar_reconhecimento():
    # Carrega o modelo YOLOv8 mais leve
    print("Carregando o modelo YOLOv8...")
    modelo = YOLO("yolov8n.pt")

    # Inicia a webcam
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Erro: Não foi possível acessar a webcam.")
        return

    print("Câmera ativada! Mostre objetos para a tela. Pressione 'q' para sair.")

    while True:
        sucesso, frame = camera.read()
        if not sucesso:
            break

        # Faz a detecção no frame atual
        resultados = modelo(frame, stream=True)

        # Desenha os quadrados na tela
        for resultado in resultados:
            frame_anotado = resultado.plot()

        # Mostra o resultado na janela
        cv2.imshow("Reconhecimento C2 - YOLOv8", frame_anotado)

        # Aperte 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    iniciar_reconhecimento()