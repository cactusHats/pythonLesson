cityA = {"東京", "名古屋", "京都", "大阪"}
cityB = {"京都", "大阪", "福岡"}

print("Aの都市名は", cityA, "です")
print("Bの都市名は", cityB, "です")

print("共通のデータは", cityA & cityB, "です")
print("Aのみのデータは", cityA - cityB, "です")
print("Bのみのデータは", cityB - cityA, "です")
print("全てのデータは", cityA | cityB, "です")