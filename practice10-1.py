import os

curdir = os.listdir(".")

print("名前\tサイズ")
for name in curdir:
    print(name, "\t", os.path.getsize(name), "バイト")