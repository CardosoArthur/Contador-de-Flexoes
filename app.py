import cv2
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

contador = 0
fase = None

cap = cv2.VideoCapture("flexao.mp4")

while True:
    ret, frame = cap.read()
    
    # Reinicia o vídeo se ele terminar
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        continue

    frame = cv2.resize(frame, (640, 480))
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = pose.process(rgb)

    if resultado.pose_landmarks:
        mp_draw.draw_landmarks(frame, resultado.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        pontos = resultado.pose_landmarks.landmark
        ombro_y = pontos[12].y
        altura_pixel = ombro_y * frame.shape[0]

        cv2.putText(frame, f"Altura Ombro: {int(altura_pixel)}", (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

        if altura_pixel > 320:
            fase = 'descendo'
        if altura_pixel < 240 and fase == 'descendo':
            fase = 'subindo'
            contador += 1

        cv2.putText(frame, f"Flexoes: {contador}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.imshow("Contador de Flexoes", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
