import numpy as np

# arr = np.array([1,2,3,4])

# print(f"Reshape to grid: {np.reshape(arr, (2,2))}")

arr = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])

# print(f"Reshape #2: {np.reshape(arr, (2,1,4))}")

# arr = np.array([[1,2], [3,4], [5,6], [7,8]])

# print(f"Transpose: {np.transpose(arr)}")
print (f"Ravel: {np.ravel(arr)}")
print (f"Flatten: {arr.flatten()}")