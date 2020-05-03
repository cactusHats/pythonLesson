import os
import datetime

curdir = os.listdir(".")

print("名前\t最終アクセス時刻")
for name in curdir:
    print(name, "\t", datetime.datetime.fromtimestamp(os.path.getatime(name)))