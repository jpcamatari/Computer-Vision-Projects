import cv2
import numpy as np

#Carregando videos
cap_web = cv2.VideoCapture('data/webcam.mp4')
cap_beach = cv2.VideoCapture('data/praia.mp4')

#Infos do video carregado
frame_width = int(cap_web.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap_web.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap_web.get(cv2.CAP_PROP_FPS)

#Define codec, dimensões e fps para salvar os videos
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
out_final = cv2.VideoWriter('output_final.mp4', fourcc, fps, (frame_width, frame_height))  # Salva o vídeo da composição final

#Dimensão da janela
window_width = 1280
window_height = 720



while True:
    ret_web, frame_web = cap_web.read()
    ret_beach, frame_beach = cap_beach.read()

    if not ret_beach or not ret_web:
        break

    lower_green = np.array([0,100,0], dtype=np.uint8)
    upper_green = np.array([100,255,100], dtype=np.uint8)

    mask = cv2.inRange(frame_web, lower_green, upper_green)

    backgroud = cv2.bitwise_and(frame_beach, frame_beach, mask=mask)

    mask_inv = np.invert(mask)

    foregroud = cv2.bitwise_and(frame_web, frame_web, mask=mask_inv)

    result = cv2.addWeighted(backgroud, 1, foregroud, 1, 0)

    out_final.write(result)

    result_resized = cv2.resize(result, (window_width, window_height))

    cv2.imshow('Resultado', result_resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        

cap_beach.release()
cap_web.release()
cv2.destroyAllWindows()