import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('HSV Trackbars')
cv2.createTrackbar('Low H', 'HSV Trackbars', 0, 179, nothing)
cv2.createTrackbar('High H', 'HSV Trackbars', 179, 179, nothing)
cv2.createTrackbar('Low S', 'HSV Trackbars', 0, 255, nothing)
cv2.createTrackbar('High S', 'HSV Trackbars', 255, 255, nothing)
cv2.createTrackbar('Low V', 'HSV Trackbars', 0, 255, nothing)
cv2.createTrackbar('High V', 'HSV Trackbars', 255, 255, nothing)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    low_h = cv2.getTrackbarPos('Low H', 'HSV Trackbars')
    high_h = cv2.getTrackbarPos('High H', 'HSV Trackbars')
    low_s = cv2.getTrackbarPos('Low S', 'HSV Trackbars')
    high_s = cv2.getTrackbarPos('High S', 'HSV Trackbars')
    low_v = cv2.getTrackbarPos('Low V', 'HSV Trackbars')
    high_v = cv2.getTrackbarPos('High V', 'HSV Trackbars')


    lower_color = np.array([low_h, low_s, low_v])
    upper_color = np.array([high_h, high_s, high_v])

    
    mask = cv2.inRange(hsv, lower_color, upper_color)


    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
