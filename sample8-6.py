#OK1
import myclass
#OK2
# import myclass as my #インポートファイルに名まえを付ける
#OK3 
# from myclass import Customer
#OK4
# from myclass import *

#OK1
pr = myclass.Customer("鈴木", 23, "mmm@nnn.nn.jp", "xxx-xxx-xxxx")
#OK2
# pr = my.Customer("鈴木", 23, "mmm@nnn.nn.jp", "xxx-xxx-xxxx")
#OK3
# pr = Customer("鈴木", 23, "mmm@nnn.nn.jp", "xxx-xxx-xxxx")
#OK4
# pr = Customer("鈴木", 23, "mmm@nnn.nn.jp", "xxx-xxx-xxxx")

nm = pr.getName()
ag = pr.getAge()
ad = pr.getAge()
tl = pr.getTel()

print(nm, "さんは", ag, "歳です")
print("アドレスは", ad, " 電話番号は", tl, "です")