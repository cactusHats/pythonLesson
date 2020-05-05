import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-8, 8, 0.1)
y1 = 3*x+5
y2 = x*x

plt.title("y=f(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)

plt.plot(x, y1, label="y=3x+5")
plt.plot(x, y2, label="x^2")
plt.legend()

plt.show()