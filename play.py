import subprocess

# 실행할 파일 리스트 (순서대로)
file_list = [
    "reset.py",
    "points_make.py",
    "mylinearregresion.py",
    "module.py"
]

for file in file_list:
    print(f"실행 중: {file}")
    subprocess.run(["python", file], check=True)
print("모든 파일 실행 완료!")