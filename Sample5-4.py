sale = [80, 60, 33, 50, 75]

i = int(input("何番目のデータを変更しますか?:"))
num = int(input("変更後のデータを入力してください:"))

print(i, "番目のデータ", sale[i], "を変更します")
sale[i] = num
print(i, "番目のデータは", sale[i], "に変更されました")