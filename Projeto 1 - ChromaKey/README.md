#Keying com OpenCV

Nesse projeto tecnico, temos a inteção de remover o fundo verde de um video, e inserir uma mascara de um backgroud no fundo utilizando a biblioteca OpenCV

<p align="center">
  <img src="data/fus%C3%A3o%20chromakey.gif" style="width: 700px; height: 400px;">
</p>

##Carregando as os videos

'''python
#Carregando videos
cap_web = cv2.VideoCapture('data/webcam.mp4')
cap_beach = cv2.VideoCapture('data/praia.mp4')
'''

##Pegando configurações de dimensões e frames por segundo e configurando saida do video unido

'''python
#Infos do video carregado
frame_width = int(cap_web.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap_web.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap_web.get(cv2.CAP_PROP_FPS)

#Define codec, dimensões e fps para salvar os videos
fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
out_final = cv2.VideoWriter('output_final.mp4', fourcc, fps, (frame_width, frame_height))  # Salva o vídeo da composição final
'''

##Loop para criar mascara em cima do fundo verde e adicionar video de backgroud frame a frame e salva-lo

Essa é a parte principal do codigo, resposavel por pegar video com backgroud verde, criar uma mascara, remover o fundo verde e adicionar frame a frame o video de backgroud da praia, e por fim salvar video.

'''python
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
    '''