v = False

for i in range(5):
    for j in range(5):
        if v is False:
            print("*", end="") #文末を""で終わらせる=改行しない
            v = True
        else:
            print("-", end="")
            v = False
    print() #改行