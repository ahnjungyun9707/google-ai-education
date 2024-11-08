import cv2
import numpy as np

cap = cv2.VideoCapture(0)

colors = {
    'Red': ([0, 100, 100], [10, 255, 255]),
    'Yellow': ([20, 100, 100], [30, 255, 255]),
    'Green': ([40, 100, 100], [70, 255, 255])
}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    for color_name, (lower, upper) in colors.items():
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
        result = cv2.bitwise_and(frame, frame, mask=mask)
        
        cv2.imshow(color_name, result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
