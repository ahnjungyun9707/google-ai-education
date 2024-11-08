# 날짜_시간 형태로 폴더를 생성하고 
# 가장 오래된 폴더 정렬해서 찾기, 지우기

import os
from datetime import datetime

# 폴더를 생성
# 현재 폴더 아래에 test폴더를 생성
# test폴더 아래에 날짜_시간 폴더를 생성

basePath = 'test/A/B'
# 폴더 만드는 함수
os.makedirs(basePath, exist_ok=True)

# 현재시간 가져오기
now = datetime.now()
#folderName = now.strftime("%Y%m%d_%h")
for hour in range(24):
    folderName = now.strftime("%Y%m%d_")
    folderName = folderName + str(hour)
    folderName = os.path.join(basePath, folderName)
    os.makedirs(basePath, exist_ok=True)

print(folderName)
