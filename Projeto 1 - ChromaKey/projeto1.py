import cv2
import numpy as np

cap_door = cv2.VideoCapture('data/door_-_89274 (540p).mp4')
cap_beach = cv2.VideoCapture('data/praia.praia.mp4')

while True:
    ret_door, frame_door = cap_door.read()
    ret_beach, frame_beach = cap_beach.read()

    if not ret_beach or not ret_door:
        break

    lower_green = np.array([0,250,0], dtype=np.uint8)
    upper_green = np.array([100,255,100], dtype=np.uint8)

    mask = cv2.inRange(frame_door, lower_green, upper_green)

    backgroud = cv2.bitwise_and(frame_beach, frame_beach, mask=mask)