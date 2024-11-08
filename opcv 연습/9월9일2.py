import cv2
import numpy as np

# 그릴 이미지 생성
img = np.ones((512, 512, 3), dtype=np.uint8) * 255
drawing = False
mode = None  # 'circle' or 'polygon'
points = []  # 다각형을 위한 점들 저장

# 마우스 이벤트 콜백 함수
def draw_shape(event, x, y, flags, param):
    global drawing, mode, points, img
    
    if event == cv2.EVENT_RBUTTONDOWN:  # 원 그리기 모드
        drawing = True
        mode = 'circle'
        cv2.circle(img, (x, y), 50, (0, 255, 0), 2)  # 원 그리기
    elif event == cv2.EVENT_LBUTTONDOWN:  # 다각형 그리기 모드
        drawing = True
        mode = 'polygon'
        points.append((x, y))  # 점 추가
        if len(points) >= 3:  # 삼각형 그리기 (3개의 점이 모였을 때)
            cv2.polylines(img, [np.array(points)], isClosed=True, color=(255, 0, 0), thickness=2)
            points = []  # 초기화
    
    if event == cv2.EVENT_RBUTTONUP or event == cv2.EVENT_LBUTTONUP:
        drawing = False

# 윈도우와 마우스 콜백 설정
cv2.namedWindow('Draw Shapes')
cv2.setMouseCallback('Draw Shapes', draw_shape)

# 이미지 출력 루프
while True:
    cv2.imshow('Draw Shapes', img)
    
    # 'r'을 누르면 이미지를 리사이징하여 선이 얼마나 뭉개지는지 확인
    if cv2.waitKey(1) & 0xFF == ord('r'):
        resized = cv2.resize(img, (256, 256), interpolation=cv2.INTER_LINEAR)
        cv2.imshow('Resized', resized)

    # 'f'을 누르면 부드럽게 필터링하여 다시 리사이징
    if cv2.waitKey(1) & 0xFF == ord('f'):
        filtered = cv2.resize(img, (256, 256), interpolation=cv2.INTER_AREA)
        cv2.imshow('Filtered Resized', filtered)

    # ESC 키로 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
