import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_mask = cv2.inRange(hsv, np.array([0, 100, 100]), np.array([10, 255, 255]))
    yellow_mask = cv2.inRange(hsv, np.array([20, 100, 100]), np.array([30, 255, 255]))
    green_mask = cv2.inRange(hsv, np.array([40, 100, 100]), np.array([70, 255, 255]))

    cv2.imshow('Red', red_mask)
    cv2.imshow('Yellow', yellow_mask)
    cv2.imshow('Green', green_mask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
