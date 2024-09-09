import cv2, sys
import numpy as np

src = cv2.imread('misson/01.png')

kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
    
sharpend = cv2.filter2D(src, -1, kernel)

cv2.imwrite('good01.png', sharpend)
cv2.imshow('src',sharpend)
cv2.waitKey()
cv2.destroyAllWindows()