place = ["東京", "名古屋", "大阪", "京都", "福岡"]
max = [32, 28, 27, 26, 27]
min = [25, 21, 20, 19, 22]

print("都市名データは", place, "です")
print("最高気温データは", max, "です")
print("最低気温データは", min, "です")

for pl, ma, mi in zip(place, max, min):
    print(pl, "の最高気温は", ma, "最低気温は", mi)