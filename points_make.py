import numpy as np
import csv
import os
from constants import NUM_POINTS, SEED, NOISE,SLOPE,Y_INTERCEPT #다른파일에서 가져오기


def make_points_csv(filepath, num_points=NUM_POINTS, seed=SEED, noise_std=NOISE, slope=SLOPE,y_intercept=Y_INTERCEPT):
    """
    랜덤 점을 생성하여 CSV로 저장합니다.
    filepath: 저장할 파일 경로
    num_points: 생성할 점 개수
    seed: 난수 시드
    noise_std: 노이즈 표준편차
    slope: y = slope * x + 5 + noise 에서의 기울기
    """

    dir_path = os.path.dirname(filepath)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)


    # 0~100 사이의 x값을 랜덤하게 num_points개 생성
    np.random.seed(seed)  # 재현성을 위해 시드 고정
    x = np.random.uniform(0, 100, num_points) #균등분포(Uniform distribution)에서 랜덤값 생성 (첫번째 인자 시작값, 두번째 인자 끝값, 세번째 인자 개수)
    noise = np.random.normal(0, noise_std, num_points) #정규분포(Normal distribution)에서 랜덤값 생성 (첫번째 인자 평균, 두번째 인자 표준편차, 세번째 인자 개수)
    y = slope * x + y_intercept + noise #y = mx + b + noise 형태로 y값 생성
    points = list(zip(x, y)) #튜플로 묶어서 리스트로 변환

    #print(points[:5]) #디버깅용

    rounded_points = [(round(px, 1), round(py, 1)) for px, py in points] #소수점 1자리까지 반올림


    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'y'])  # 헤더 추가
        writer.writerows(rounded_points)



if __name__ == "__main__":
    make_points_csv('./data/points.csv')