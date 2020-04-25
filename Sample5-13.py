city = ["東京", "名古屋", "大阪", "京都"]
sale = [80, 60, 22, 50, 75]

print("都市データは", city, "です")
print("売上データは", sale, "です")

print("---")
for d in zip(city, sale):
    print(d)

print("---")
for c, s in zip(city, sale):
    print("都市名は", c, "売上は", s)