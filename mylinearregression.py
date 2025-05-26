from error_calc import save_distances_and_errors_to_csv as distances
import csv
import math
from constants import NUM_ITERATIONS, NUM_ANGLE_DIVISIONS

#point.csv 파일에서 점들을 읽어오는 함수
def read_points_from_csv(filepath):
    points = []
    with open(filepath, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # 헤더 건너뛰기
        for row in reader:
            x, y = float(row[0]), float(row[1])
            points.append((x, y))
    return points

# 각도와 절편 후보의 범위를 계산하는 함수
def get_search_range(center, width, divisions):
    half = divisions // 2
    return [center + (k - half) * width for k in range(divisions)]

def main():
    points = read_points_from_csv('./data/points.csv')
    y_values = [p[1] for p in points] # y값 리스트 생성
    b_range = max(y_values) # 절편범위
    angle_range = 180 # 각도범위

    results = [] # 결과를 저장할 리스트
    angles_list, b_list = [], [] # 절편과 각도 저장 리스트

    # 초기 각도, 절편 후보 생성
    angles = [i * (angle_range / NUM_ANGLE_DIVISIONS) for i in range(NUM_ANGLE_DIVISIONS)]
    bs = [i * (b_range / NUM_ANGLE_DIVISIONS) for i in range(NUM_ANGLE_DIVISIONS)]

    for i in range(NUM_ITERATIONS):
        iter_results = [] # 각 반복에서의 결과를 저장할 리스트

        for a_idx, angle in enumerate(angles): #enumerate 인덱스와 값을 함께 가져옴
            slope = math.tan(math.radians(angle))
            for b_idx, b in enumerate(bs):
                mse, mae = distances(points, slope, b)
                iter_results.append((a_idx, b_idx, angle, slope, b, mse, mae))

        # 최소 MSE 조합 찾기
        min_result = min(iter_results, key=lambda x: x[5])
        min_angle, min_b = min_result[2], min_result[4]
        angles_list.append(min_angle)
        b_list.append(min_b)
        results.append((i, min_angle, min_b, min_result[5], min_result[6]))

        # 탐색 범위 축소
        angle_range /= NUM_ANGLE_DIVISIONS
        b_range /= NUM_ANGLE_DIVISIONS
        angles = get_search_range(min_angle, angle_range, NUM_ANGLE_DIVISIONS)
        bs = get_search_range(min_b, b_range, NUM_ANGLE_DIVISIONS)

    # 결과 저장
    with open('./data/myregression_result.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['iteration', 'angle', 'b', 'min_mse', 'min_mae'])
        for row in results:
            writer.writerow([row[0], round(row[1], 5), round(row[2], 5), round(row[3], 5), round(row[4], 5)])

    print("각도:", angles_list[-1])
    print("y절편:", b_list[-1])

if __name__ == "__main__":
    main()