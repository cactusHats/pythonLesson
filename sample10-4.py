import json

f = open("Sample.json", "r", encoding="utf-8")
data = json.load(f)
print(data)
f.close()