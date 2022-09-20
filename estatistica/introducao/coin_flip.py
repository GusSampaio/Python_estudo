import matplotlib.pyplot as plt
import numpy as np

def coinFlip(size):
    flips = np.random.randint(0, 2, size=size)
    return flips.mean()

coinFlip = np.frompyfunc(coinFlip, 1, 1)

xmin, xmax, dx = 1, 5000, 1
x = np.arange(xmin, xmax, dx)
y = coinFlip(x)
print(y)
plt.plot(x, y)
plt.show()
