import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 100, 101)

altitude = np.zeros(101)

for i in range(len(time)):
    altitude[i] = .01 * time[i]**2

plt.figure(figsize=(8, 6))
plt.plot(time, altitude, 'b-', label='Spacecraft Altitude')
plt.title('Spacecraft Ascent: Altitude vs. Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Altitude (kilometers)')
plt.grid(True)
plt.legend()
plt.show()