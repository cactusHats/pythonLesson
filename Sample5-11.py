data = [1, 2, 3, 4, 5]
print("現在のデータは", data, "です")

# 逆にアクセスできて，表示も可能
for d in data[::-1]:
    print(d)
print("data[::-1]は",data[::-1],"です")
print("現在のデータは", data, "です")

# 逆にアクセスできるが，表示はアドレス
for d in reversed(data):
    print(d)
print("reversed(data)は",reversed(data),"です")
print("現在のデータは", data, "です")

# 元データ自体を入れ替える
data.reverse()
print("現在のデータは", data, "です")
