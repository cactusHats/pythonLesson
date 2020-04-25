sale = int(input("売り上げを入力してください:"))

if sale >= 100:
    print("売り上げは好調です")
elif sale >= 50:
    print("売り上げは普通です")
else:
    print("売り上げは低調です")

print("処理を終了します")