sale = [80, 60, 22, 50, 75]
print("現在のデータは", sale, "です")

print("最大値:", max(sale))
print("最小値:", min(sale))
print("合計値:", sum(sale))

 # 元データは並び変えない
print("ソート(昇順):",sorted(sale))
print("ソート(降順):",sorted(sale, reverse=True))
print("現在のデータは", sale, "です")

# 元データを並び変える
sale.sort()
print("現在のデータは", sale, "です")

sale.sort(reverse=True)
print("現在のデータは", sale, "です")