import cv2
import os
import numpy as np
from glob import glob

def getImageList():
    basePath = os.getcwd()
    dataPath = os.path.join(basePath, 'images')
    fileNames = glob(os.path.join(dataPath, '*.jpg'))
    return fileNames

def drawROI(cpy, corners):
    cpy = cpy.copy()
    line_c = (128, 128, 255)
    lineWidth = 2
    for corner in corners:
        cv2.rectangle(cpy, tuple(corner[0]), tuple(corner[1]), color=line_c, thickness=lineWidth)
    disp = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)
    return disp

def onMouse(event, x, y, flags, param):
    global startPt, img, ptList, cpy, txtWrData
    if event == cv2.EVENT_LBUTTONDOWN:
        startPt = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        pt = [startPt, (x, y)]
        ptList.append(pt)
        txtWrData = str(ptList)
        cpy = drawROI(cpy, ptList)
        startPt = None
        cv2.imshow('label', cpy)
    elif event == cv2.EVENT_MOUSEMOVE:
        if startPt:
            temp_cpy = drawROI(cpy, ptList + [[startPt, (x, y)]])
            cv2.imshow('label', temp_cpy)

def convertToYOLO(box, img_shape):
    x1, y1 = box[0]
    x2, y2 = box[1]
    img_h, img_w = img_shape[:2]
    
    center_x = (x1 + x2) / 2 / img_w
    center_y = (y1 + y2) / 2 / img_h
    width = (x2 - x1) / img_w
    height = (y2 - y1) / img_h

    return (center_x, center_y, width, height)

ptList = []
startPt = None
cpy = []
txtWrData = ""

fileNames = getImageList()
current_idx = 0

img = cv2.imread(fileNames[current_idx])
cv2.namedWindow('label')
cv2.setMouseCallback('label', onMouse)

while True:
    cv2.imshow('label', img)
    key = cv2.waitKey()

    if key == 27:  # ESC
        break
    elif key == ord('s'):
        filename, ext = os.path.splitext(fileNames[current_idx])
        txtFilename = filename + '.txt'
        with open(txtFilename, 'w') as f:
            for box in ptList:
                yolo_box = convertToYOLO(box, img.shape)
                f.write(f"0 {yolo_box[0]} {yolo_box[1]} {yolo_box[2]} {yolo_box[3]}\n")
        print(f'Saved: {txtFilename}')
    elif key == ord('c'):
        ptList = []
        cpy = img.copy()
        cv2.imshow('label', cpy)
    elif key == 81:  # Left arrow key
        current_idx = max(0, current_idx - 1)
        img = cv2.imread(fileNames[current_idx])
        ptList = []
        cpy = img.copy()
        cv2.imshow('label', cpy)
    elif key == 83:  # Right arrow key
        current_idx = min(len(fileNames) - 1, current_idx + 1)
        img = cv2.imread(fileNames[current_idx])
        ptList = []
        cpy = img.copy()
        cv2.imshow('label', cpy)

cv2.destroyAllWindows()
