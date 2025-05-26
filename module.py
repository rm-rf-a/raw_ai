import numpy as np
import csv
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error
import math

def read_points_from_csv(filepath):
    points = []
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 헤더 건너뛰기
        for row in reader:
            x, y = float(row[0]), float(row[1])
            points.append((x, y))
    return points



if __name__ == "__main__":
    # 데이터 읽기
    points = read_points_from_csv('./data/points.csv')
    X = np.array([p[0] for p in points]).reshape(-1, 1)
    y = np.array([p[1] for p in points])

    # 선형회귀 모델 학습
    model = LinearRegression()
    model.fit(X, y)

    # 예측 및 평가
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    mae = mean_absolute_error(y, y_pred)

    slope = model.coef_[0]
    angle_deg = math.degrees(math.atan(slope))  
    intercept = model.intercept_

    with open('./data/module_result.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['angle', 'b', 'mse', 'mae'])
        writer.writerow([round(angle_deg, 5), round(intercept, 5), round(mse, 5), round(mae, 5)])