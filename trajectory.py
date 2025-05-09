import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(0, 10, 100)
x = np.cos(t)
y = np.sin(t)
z = t / 2

traj = np.zeros((100, 3), dtype=np.float64)
traj[:, 0] = x
traj[:, 1] = y
traj[:, 2] = z

z_threshold = 1.0
indexes = np.where(traj[:, 2] < z_threshold)[0]
low_altitude_points = traj[indexes, :]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, 'b-', linewidth=2)
ax.scatter(low_altitude_points[:, 0], low_altitude_points[:, 1], low_altitude_points[:, 2], c='red', s=50, label = 'low altitude')
ax.set_xlabel('km')
ax.set_ylabel('km')
ax.set_zlabel('km')

plt.show()