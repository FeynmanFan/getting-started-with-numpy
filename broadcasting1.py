import numpy as np

a = np.array([1, 2, 3])
b = 2
result = a + b
print(result)
print(f"A shape: {0}", np.shape(a))
print(f"B shape: {0}", np.shape(b))

a = np.array([[1,2,3], [4,5,6]])
b = np.array([0, 5, 10])

# error
result = a + b

print (result)
print(f"A shape: {0}", np.shape(a))
print(f"B shape: {0}", np.shape(b))