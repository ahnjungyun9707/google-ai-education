import cv2, sys
import numpy as np

# 화살표를 누르면 원이 이동되는 어플
width, height = 512, 512
# 초기의 원의 좌표와 반지름
x,y,R = 256, 256, 50

direction = 0


# main
while True:
    # 기본 waitKeyEx + Extention키 입력까지 받아들임
    key = cv2.waitKeyEx(30) #timeout=30ms
    # 종료조건
    if key == 27: #ESC
        break
    # right key
    elif key == 0X270000:
        direction = 0
        x+=10
    # down key
    elif key == 0X280000:
        direction = 1
        y+=10
    # left key
    elif key == 0X250000:
        direction = 2
        x-=10
    # up key
    elif key == 0X260000:
        direction = 3
        y-=10
    
    # 빈 캔버스 생성
    img = np.zeros((width, height, 3), np.uint8)+255
    # 원을 그린다. img에 (x,y)좌표에 , 반지름R로, 빨간색으로 안을 채워서 -1
    cv2.circle(img, (x,y), R, (255,0,0), -1)
    cv2.imshow('img', img)

cv2.destroyAllWindows()
    