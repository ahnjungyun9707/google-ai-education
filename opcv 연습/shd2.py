import cv2
import numpy as np


cap = cv2.VideoCapture(0)


lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

lower_yellow = np.array([20, 100, 100])
upper_yellow = np.array([30, 255, 255])

lower_green = np.array([40, 100, 100])
upper_green = np.array([70, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    red_result = cv2.bitwise_and(frame, frame, mask=red_mask)
    yellow_result = cv2.bitwise_and(frame, frame, mask=yellow_mask)
    green_result = cv2.bitwise_and(frame, frame, mask=green_mask)

    cv2.imshow('Original', frame)
    cv2.imshow('Red', red_result)
    cv2.imshow('Yellow', yellow_result)
    cv2.imshow('Green', green_result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
