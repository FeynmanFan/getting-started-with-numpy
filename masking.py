import numpy as np

x = np.array([-2, -1, 1,2,5])

mask = x > 0

print(x[mask])

print(x[x > 0])

mask = x % 2 == 0

print(x[mask])