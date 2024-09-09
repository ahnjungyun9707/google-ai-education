import cv2, sys
import numpy as np

def translate(scr, x_move=0, y_move=0):
    
    # 이미지의 이동 변환 x->200, y->100만큼 이동
    # 이동 변환 행렬
    h, w = src.shape[:2]   
    aff = np.array([[1, 0, 200],[0, 1, 100]], dtype=np.float32)
    # 변환후에 출력되는 배열의 크기 (입력되는 src이미지의 크기를 그대로 출력)
    dst = cv2.warpAffine(src, aff, (h+y_move, w+x_move))
    return dst

def shear(src, x_shear=0, y_shear=0):
    if x_shear>0 and y_shear==0:
        aff = np.array([[1, x_shear, 0],[0, 1, 0]], dtype=np.float32)
        h, w = src.shape[:2]
        dst = cv2.warpAffine(src, aff, (w + int(h * x_shear, h)))
    elif y_shear>0 and x_shear==0:
        aff = np.array([[1, 0, 0],[y_shear, 1, 0]], dtype=np.float32)
        h, w = src.shape[:2]
        dst = cv2.warpAffine(src, aff, (w + int(h * y_shear), h))
    return dst
    
def scale(src, x_scale, y_scale):
    aff = np.array([[x_scale, 0, 0],[0, y_scale, 0]], dtype=np.float32)
    h, w = src.shape[:2]
    dst = cv2.warpAffine(src, aff, (w, h))
    return dst

src = cv2.imread('rose.bmp')

if src is None:
    sys.exit('Image load failed')
    

#dst = translate(src,50,50)  
#dst = shear(src, 0.5, 0)
#dst = scale(src, 0, 0.5)
# 512x512 -> 1024X1024 해상도로 설정
#dst = cv2.resize(src,(1024,1024))
# 비율로 설정(해상도x)
dst1 = cv2.resize(src,(0,0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
dst2 = cv2.resize(src,(0,0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
dst3 = cv2.resize(src,(0,0), fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)
    
cv2.imshow('src',src)
cv2.imshow('INTER_CUBIC',dst1)
cv2.imshow('INTER_NEAREST',dst2)
cv2.imshow('INTER_LANCZOS4',dst3)
cv2.waitKey()
cv2.destroyAllWindows()