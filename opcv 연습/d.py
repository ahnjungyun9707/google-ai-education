import cv2

# 이미지 불러오기
image = cv2.imread('misson/01.png') 

# 노이즈 제거 방식 선택 (예시: Fast Means Denoising)
# 다양한 방식을 적용하고 비교해 보세요!
denoised_image = cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21) 

# 결과 이미지 저장
cv2.imwrite('denoised_image.jpg', denoised_image)