import matplotlib.pyplot as plt
import random

data = []

for i in range(1000):
    data.append(random.normalvariate(0,10))

plt.title("Histgram")
plt.hist(data,bins=50)
plt.show()