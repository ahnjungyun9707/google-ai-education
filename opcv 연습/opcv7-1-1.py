import cv2, sys
import os
from glob import glob

# 0. 파일 목록 읽기(data 폴더 *.jpg -> 리스트)
def getImageList():    
    # 현재 작업 디렉토리 확인
    basePath = os.getcwd()
    dataPath = os.path.join(basePath, 'dat/')
    filenames = glob(os.path.join(dataPath, '*.jpg'))
    
    if len(filenames) == 0:
        print("No images found in the directory:", dataPath)
    return filenames

# corners : 좌표(startPt, endPt)
# 2개 좌표를 이용해서 직사각형 그리기
def drawROI(img, corners):
    # 박스를 그릴 레이어를 생성 : cpy
    cpy = img.copy()
    line_c = (128, 128, 255)
    lineWidth = 2
    cv2.rectangle(cpy, corners[0], corners[1], color=line_c, thickness=lineWidth)
    disp = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)
    return disp

# 마우스 콜백 함수 정의
def onMouse(event, x, y, flags, param):
    global startPt, endPt, img, drawing
    
    cpy = img.copy()
    
    # 마우스가 눌리면 시작점 기록
    if event == cv2.EVENT_LBUTTONDOWN:
        startPt = (x, y)
        drawing = True
    
    # 마우스 이동 중, 박스 미리보기
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            endPt = (x, y)
            cpy = drawROI(img, [startPt, endPt])
            cv2.imshow('label', cpy)

    # 마우스를 떼면 종료점 기록 및 박스 그리기 완료
    elif event == cv2.EVENT_LBUTTONUP:
        endPt = (x, y)
        drawing = False
        img = drawROI(img, [startPt, endPt])
        cv2.imshow('label', img)

# 전역 변수 초기화
startPt = None
endPt = None
drawing = False

# 파일 목록 가져오기
filenames = getImageList()

# 이미지 파일이 있는지 확인
if len(filenames) > 0:
    # 첫 번째 이미지 불러오기
    img = cv2.imread(filenames[0])

    # 이미지 로드 여부 확인
    if img is None:
        print("Failed to load image:", filenames[0])
    else:
        cv2.namedWindow('label')
        cv2.setMouseCallback('label', onMouse)

        while True:
            cv2.imshow('label', img)
            key = cv2.waitKey(1)

            # ESC 키를 누르면 종료
            if key == 27:
                break

        cv2.destroyAllWindows()
else:
    print("No image files to load.")

