import csv

# 当環境では文字エンコーディングが必要
f = open("Sample.csv", "r", encoding="utf-8")
rd = csv.reader(f)

for row in rd:
    for col in row:
        print(col, end=",")
    print()
f.close()