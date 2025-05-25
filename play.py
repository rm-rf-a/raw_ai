import subprocess
import os

base_dir = r"c:경로 알아 넣으쇼"

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