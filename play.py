import subprocess
import os

base_dir = r"C:\Users\ballo\OneDrive\문서\raw_ai\Linearregression"

file_list = [
    os.path.join(base_dir, "reset.py"),
    os.path.join(base_dir, "points_make.py"),
    os.path.join(base_dir, "mylinearregression.py"),
    os.path.join(base_dir, "module.py")
]

for file in file_list:
    print(f"실행 중: {file}")
    subprocess.run(["python", file], check=True)
print("모든 파일 실행 완료!")