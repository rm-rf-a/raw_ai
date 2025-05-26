import csv
import os


def reset_csv_files():
    # 폴더가 없으면 생성
    dir_path = './data'
    os.makedirs(dir_path, exist_ok=True)

    # points.csv 초기화 (헤더만)
    with open(os.path.join(dir_path, 'points.csv'), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['x', 'y'])

    # myregression_result.csv 초기화 (헤더만)
    with open(os.path.join(dir_path, 'myregression_result.csv'), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # myregression_result.csv의 헤더
        writer.writerow(['iteration', 'angle', 'b', 'min_mse', 'min_mae'])

    # module_result.csv 초기화 (헤더만)
    with open(os.path.join(dir_path, 'module_result.csv'), 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # module_result.csv의 헤더
        writer.writerow(['angle', 'b', 'mse', 'mae'])


if __name__ == "__main__":
    reset_csv_files()