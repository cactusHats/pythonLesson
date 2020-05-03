import re
ptr = "\.(csv|html|py)$"
str = ["Sample.csv", "Sample.exe", "Sample.py", "Sample.html"]

pattern = re.compile(ptr)
for valuestr in str:
    # valuestrにコンパイルした文字列があったら.txtに置換する．
    res = pattern.sub(".txt", valuestr)
    msg = "(変換前)" + valuestr + "(変換後)" + res
    print(msg)