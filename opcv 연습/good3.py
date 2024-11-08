import cv2, os
from glob import glob

def getImageList(): 
    return glob(r'C:\Users\SBA\Desktop\googleai\dat\*.jpg')

def convertToYOLO(box, shape): 
    h, w = shape[:2]
    return [(box[0][i]+box[1][i])/2/w if i%2==0 else (box[0][i]+box[1][i])/2/h for i in range(2)] + [(box[1][0]-box[0][0])/w, (box[1][1]-box[0][1])/h]

fileNames = getImageList()
if not fileNames:
    print("이미지가 없단다 아가야")
    exit()

img, boxes, sp = cv2.imread(getImageList()[0]), [], None
if img is None:
    print("에러가 났다 아가야")
    exit()

cv2.namedWindow('label')
cv2.setMouseCallback('label', lambda e, x, y, f, p: [boxes.append([sp, (x, y)]) if e == cv2.EVENT_LBUTTONUP else None, setattr(globals(), 'sp', (x, y)) if e == cv2.EVENT_LBUTTONDOWN else None])

while True:
    if img is None:
        cv2.imshow('label', img)
    k = cv2.waitKey()
    if k == 27: break
    elif k == ord('s'): 
        with open('labels.txt', 'w') as f:
            f.write('\n'.join(f"0 {' '.join(map(str, convertToYOLO(b, img.shape)))}" for b in boxes))
cv2.destroyAllWindows()
