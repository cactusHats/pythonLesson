import statistics

data = [8,17,0,11,6,21,16,6,17,11,7,9,6,13,12,16,3,14,13,12]

print("平均値：", statistics.mean(data))
print("中央値：", statistics.median(data))
print("最頻値：", statistics.mode(data))
print("分散：", statistics.pvariance(data))
print("標準偏差：", statistics.pstdev(data))