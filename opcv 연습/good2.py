import cv2, os
from glob import glob

def getImageList(): return glob(os.path.join(os.getcwd(), 'images', '*.jpg'))
def drawROI(cpy, corners): return cv2.addWeighted(img, 0.3, cpy, 0.7, 0)
def convertToYOLO(box, img_shape): return ((sum(box[0]) / 2) / img_shape[1], (sum(box[1]) / 2) / img_shape[0], abs(box[1][0] - box[0][0]) / img_shape[1], abs(box[1][1] - box[0][1]) / img_shape[0])

def onMouse(event, x, y, flags, param):
    global startPt, img, ptList, cpy
    if event == cv2.EVENT_LBUTTONDOWN: startPt = (x, y)
    elif event == cv2.EVENT_LBUTTONUP: ptList.append([startPt, (x, y)]); cpy = drawROI(cpy, ptList); cv2.imshow('label', cpy)

img, ptList, startPt = cv2.imread(getImageList()[0]), [], None
cv2.namedWindow('label'), cv2.setMouseCallback('label', onMouse)

while True:
    cv2.imshow('label', img)
    key = cv2.waitKey()
    if key == 27: break
    elif key == ord('s'):
        with open(os.path.splitext(fileNames[0])[0] + '.txt', 'w') as f:
            for box in ptList: f.write(f"0 {' '.join(map(str, convertToYOLO(box, img.shape)))}\n")
    elif key == ord('c'): ptList, cpy = [], img.copy()

cv2.destroyAllWindows()