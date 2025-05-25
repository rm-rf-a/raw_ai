from error_calc import save_distances_and_errors_to_csv as distances
import numpy as np
import csv
from constants import NUM_ITERATIONS,NUM_ANGLE_DIVISIONS
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

points = read_points_from_csv('./Linearregression/points.csv')


y_values = [p[1] for p in points]
b_range = max(y_values)

results = []
angles_list = []
b_list = []
angle_range = 180  # 각도 범위

angles = [i * (angle_range / NUM_ANGLE_DIVISIONS) for i in range(NUM_ANGLE_DIVISIONS)]
bs = [i * (b_range / NUM_ANGLE_DIVISIONS) for i in range(NUM_ANGLE_DIVISIONS)]

for i in range(NUM_ITERATIONS):
    for a_idx, angle in enumerate(angles):
        slope = math.tan(math.radians(angle))
        for b_idx, b in enumerate(bs):
            mse, mae = distances(points, slope, b)
            results.append((i, a_idx, b_idx, angle, slope, b, mse, mae))
    # 이번 반복에서 최소 MSE 조합 찾기
    min_result = min(results[-(NUM_ANGLE_DIVISIONS**2):], key=lambda x: x[6])
    min_mse = min_result[6]
    angles_max = min_result[3]
    b_max = min_result[5]

    angles_list.append(angles_max)
    b_list.append(b_max)
    # 각도, y절편 범위를 점점 줄여가며 4등분
    angle_range = angle_range / NUM_ANGLE_DIVISIONS
    b_range = b_range / NUM_ANGLE_DIVISIONS
    angles = [angles_max + (k - NUM_ANGLE_DIVISIONS//2) * angle_range for k in range(NUM_ANGLE_DIVISIONS)]
    bs = [b_max + (k - NUM_ANGLE_DIVISIONS//2) * b_range for k in range(NUM_ANGLE_DIVISIONS)]

# 결과 저장
with open('./Linearregression/myregression_result.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['iteration', 'angle', 'b', 'min_mse', 'min_mae'])
    for idx, (angle, b) in enumerate(zip(angles_list, b_list)):
        # 해당 반복에서 angle, b에 해당하는 mae도 함께 저장
        min_row = [r for r in results if r[0] == idx and r[3] == angle and r[5] == b][0]
        min_mse = min_row[6]
        min_mae = min_row[7]
        writer.writerow([idx, round(angle, 5), round(b, 5), round(min_mse, 5), round(min_mae, 5)])

print("최종 최소 MSE 각도:", angles_max)
print("최종 최소 MSE y절편:", b_max)