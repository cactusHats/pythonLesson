import sqlite3

conn = sqlite3.connect("pdb.db")
c = conn.cursor()

# 以下の条件によって抽出されたイテレータが得られるってことか
itr = c.execute("SELECT * FROM product WHERE name = '鉛筆'")

for row in itr:
    print(row)

conn.close()