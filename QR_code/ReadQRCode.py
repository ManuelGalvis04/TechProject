import cv2
from pyzbar.pyzbar import decode
import numpy as np

def read_qr_code_from_camera():
    # Iniciar la captura de video desde la cámara
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: No se puede acceder a la cámara.")
        return

    while True:
        # Leer un frame de la cámara
        ret, frame = cap.read()
        if not ret:
            print("Error: No se pudo leer el frame.")
            break

        # Decodificar el código QR
        decoded_objects = decode(frame)

        for obj in decoded_objects:
            # Dibujar el rectángulo alrededor del código QR
            points = obj.polygon
            if len(points) > 4: 
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                hull = list(map(tuple, np.squeeze(hull)))
            else:
                hull = points
            
            n = len(hull)
            for j in range(n):
                cv2.line(frame, hull[j], hull[(j + 1) % n], (0, 255, 0), 3)

            # Mostrar los datos decodificados
            print(f"Tipo: {obj.type}")
            print(f"Datos: {obj.data.decode('utf-8')}")
            print(f"Rectángulo de coordenadas: {obj.rect}")
            print()

        # Mostrar el frame con el código QR detectado
        cv2.imshow('QR Code Scanner', frame)

        # Salir del loop si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar la captura y cerrar las ventanas
    cap.release()
    cv2.destroyAllWindows()

# Ejemplo de uso
read_qr_code_from_camera()
