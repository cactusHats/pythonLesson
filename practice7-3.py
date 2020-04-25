#ジェネレータ
def makex(x):
    while True:
        yield x #return的な役割，でも処理は続く
        x = x+1

start = int(input("開始値(整数)を入力してください:"))
stop = int(input("終了値(整数)を入力してください:"))

for n in makex(start):
    if n >= stop:
        break
    print(n)