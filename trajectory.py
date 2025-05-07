import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(0, 10, 100)
x = np.cos(t)
y = np.sin(t)
z = t / 2

traj = np.column_stack((x, y, z))

print("Trajectory shape: ", traj.shape)
print("Time shape: ", t.shape)
print("Trajectory Size:", traj.size)
print("Time size: ", t.size)
print("Trajectory Data Type: ", traj.dtype)
print("Time Data Type: ", t.dtype)
print("Trajectory Dimensions:", traj.ndim)
print("Time Dimensions:", t.ndim)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, 'b-', linewidth=2)
ax.set_xlabel('km')
ax.set_ylabel('km')
ax.set_zlabel('km')

plt.show()