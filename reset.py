import csv

# points.csv 초기화 (헤더만)
with open('./Linearregression/points.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'y'])

# angles_list.csv 초기화 (헤더만)
with open('./Linearregression/myregression_result.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['iteration', 'angle'])


with open('./Linearregression/module_result.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['iteration', 'angle'])