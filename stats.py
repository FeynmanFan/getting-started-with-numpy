import numpy as np

data = np.array([30, 30, 30, 30, 30, 20, 25, 35, 40, 60, 70, 80, 90, 100])

arithmetic_mean = np.mean(data)
bincount = np.bincount(data)
mode = bincount.argmax()
std_dev = np.std(data)
median = np.median(data)
sum = np.sum(data)
min = np.min(data)
max = np.max(data)

print("Dataset:", data)
print(f"Arithmetic Mean (Average): {arithmetic_mean:.2f}")
print(f"Bin count: {bincount}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {std_dev:.2f}")
print(f"Median: {median:.2f}")
print(f"Sum: {sum:.2f}")
print(f"Min: {min:.2f}")
print(f"Max: {max:.2f}")