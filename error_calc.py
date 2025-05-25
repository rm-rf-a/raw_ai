import numpy as np
import csv 

def save_distances_and_errors_to_csv(points, m, b):
    """
    여러 점들과 직선 y = mx + b 사이의 거리, 거리제곱, MAE, MSE를 CSV로 저장
    """
    points = np.array(points) #넘파이로 만들기
    x = points[:, 0] #[x,y] 에서 0번 인덱스는 x ,1번 인덱스는 y이니까 x만 추출 y만 추출 (넘파이배열)
    y = points[:, 1]
    numerator = np.abs(m * x - y + b) #abs절댓값계산
    denominator = np.sqrt(m**2 + 1) #sqrt squareroot(제곱근)의 약자, 루트계산
    distances = numerator / denominator #점과 직선사이 거리 계산
    squared_distances = distances ** 2 #거리 제곱
    mse = np.mean(squared_distances) #거리 제곱의 평균(MSE)
    mae = np.mean(distances) #거리의 평균(MAE)

    """
    with open('./Linearregression/error.csv', 'a', newline='', encoding='utf-8') as f: # 'a' 모드로 열어서 기존 파일에 추가
        writer = csv.writer(f)
        writer.writerow(['x', 'y', 'distance', 'distance_squared']) #헤더 추가
        for (px, py), d, d2 in zip(points, distances, squared_distances):
            writer.writerow([round(px, 5), round(py, 5), round(d, 5), round(d2, 5)])
        writer.writerow([])  # 빈 줄
        writer.writerow(['MSE', '', '', round(mse, 5)]) #MSE 저장
        writer.writerow(['MAE', '', '', round(mae, 5)]) #MAE 저장
    """
    
    return mse, mae 