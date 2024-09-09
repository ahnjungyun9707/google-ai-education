import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

img = np.full((512, 512, 3), 255, np.uint8)
pts = []

def draw(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:  
        cv2.circle(img, (x, y), 50, (0, 255, 0), 2)
    elif event == cv2.EVENT_LBUTTONDOWN:  
        pts.append((x, y))
        if len(pts) == 3:  
            cv2.polylines(img, [np.array(pts)], True, (255, 0, 0), 2)
            pts.clear()
        elif len(pts) == 4: 
            cv2.polylines(img, [np.array(pts)], True, (0, 0, 255), 2)
            pts.clear()

cv2.namedWindow('Draw')
cv2.setMouseCallback('Draw', draw)

while True:
    cv2.imshow('Draw', img)
    k = cv2.waitKey(1)
    if k == ord('r'):
        cv2.imshow('Resized', cv2.resize(img, (256, 256)))
    elif k == ord('f'):
        cv2.imshow('Filtered', cv2.resize(img, (256, 256), interpolation=cv2.INTER_AREA))
    elif k == 27:
        break

cv2.destroyAllWindows()

