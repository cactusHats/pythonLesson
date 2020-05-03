file = ["Sample.csv", "Sample.exe", "Sample.py1", "Sample.py1", "Sample.html"]

print("ファイルリストは以下です")
for val in file:
    print(val)

key = input("拡張子を入力してください")

print("該当するファイルのリストは以下です")
for val in file:
    res = val.find(key)
    if res != -1:
        print(val)