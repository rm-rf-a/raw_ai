import numpy as np
import csv

from constants import  NUM_POINTS,SEED,NOISE #다른파일에서 가져오기

##############################################################################################
# 0~100 사이의 x값을 랜덤하게 100개 생성
np.random.seed(SEED)  # 재현성을 위해 시드 고정
x = np.random.uniform(0, 100, NUM_POINTS) #균등분포(Uniform distribution)에서 랜덤값 생성 (첫번째 인자 시작값, 두번째 인자 끝값, 세번째 인자 개수)

# y = 0.8x + 5 + 노이즈(정규분포, 표준편차 5)
noise = np.random.normal(0, NOISE, NUM_POINTS) #정규분포(Normal distribution)에서 랜덤값 생성 (첫번째 인자 평균, 두번째 인자 표준편차, 세번째 인자 개수)
y = 0.8 * x + 5 + noise

# (x, y) 형태의 점 리스트로 변환
points = list(zip(x, y)) #튜플로 묶어서 리스트로 변환

#print(points[:5]) #디버깅용으로 처음 5개 점 출력

rounded_points = [(round(px, 1), round(py, 1)) for px, py in points] #소수점 1자리까지 반올림

with open('./Linearregression/points.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'y'])  # 헤더 추가
    writer.writerows(rounded_points)
##############################################################################################