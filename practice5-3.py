score = [74, 85, 69, 77, 81]
print("テストの点は", score, "です")

nscore = [n for n in score if n >= 80]
print("80点以上は", nscore)
print("80点以上の人数は", len(nscore) ,"人です")