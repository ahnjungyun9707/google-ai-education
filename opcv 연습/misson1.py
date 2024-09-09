import cv2, sys
import numpy as np

src = cv2.imread('misson/05.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

src1 = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
src_f = src1[:, :, 0].astype(np.float32)
blr = cv2.GaussianBlur(src_f, (0,0), 2.0)
src1[:, :, 0] = np.clip(2. * src_f - blr, 0, 255).astype(np.uint8)
dst = cv2.cvtColor(src1, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

#언샤프