import datetime

dt = datetime.datetime.now()
print("現在は", dt, "です")
print("年：", dt.year)
print("月：", dt.month)
print("日：", dt.second)

# 1日後
dt = dt + datetime.timedelta(days=1)
# 2時間後
# dt = dt + datetime.timedelta(hours=2)
# 4週間後
# dt = dt + datetime.timedelta(weeks=4)

print("1日後は", dt, "です")