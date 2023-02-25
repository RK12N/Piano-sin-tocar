import cv2
import mediapipe as mp
import pygame
import time


# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands

# Configurar la cámara
cap = cv2.VideoCapture(0)

def re():
    pygame.init()
    sound = pygame.mixer.Sound("Re.wav")
    sound.play()
    return

# Inicializar el detector de manos
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:

    while True:
        # Leer la imagen desde la cámara
        ret, frame = cap.read()

        # Convertir la imagen de BGR a RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detección de manos
        results = hands.process(image)

        # Dibujar los puntos de las manos detectadas
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Obtener la posición de cada punto de la mano
                thumb_tip = (int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image.shape[1]), 
                             int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image.shape[0]))
                thumb_mcp = (int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].x * image.shape[1]), 
                             int(hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_MCP].y * image.shape[0]))
                index_tip = (int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image.shape[1]), 
                             int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image.shape[0]))
                
                # Dibujar un círculo en el dedo pulgar
                cv2.circle(frame, thumb_tip, 5, (0, 255, 0), -1)
                
                # Identificar cuando solo el dedo pulgar está levantado
                if thumb_tip[1] < thumb_mcp[1] and thumb_tip[1] < index_tip[1]:
                    # Llamar a la función que desees
                    time.sleep(0.50)

                    re()
                    

        # Mostrar la imagen en la pantalla
        cv2.imshow("Hand Tracking", frame)

        # Salir del bucle si se presiona la tecla "q"
        if cv2.waitKey(1) == ord("q"):
            break

# Liberar la cámara y cerrar la ventana
cap.release()
cv2.destroyAllWindows()
