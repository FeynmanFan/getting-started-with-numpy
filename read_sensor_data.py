import pandas as pd
import numpy as np

df = pd.read_csv('sensor_data.txt')
print("Original DataFrame:")
print(df)

pivot_temp = df.pivot(index='time', columns='sensor_id', values='temp')
pivot_rad = df.pivot(index='time', columns='sensor_id', values='rad')

temp_array = pivot_temp.to_numpy()
rad_array = pivot_rad.to_numpy()

sensor_array = np.dstack((temp_array, rad_array))

print("\nReshaped 3D NumPy array (time, sensors, measurements):")
print(sensor_array.round(2))
print("Shape:", sensor_array.shape)

flattened = np.ravel(sensor_array)
print(flattened)
flat_array = flattened.reshape(-1, 2)
print(flat_array)

df_from_array = pd.DataFrame(
    flat_array,
    columns=['temp', 'rad'],
    index=pd.MultiIndex.from_product(
        [[0, 1, 2, 3], ['S1', 'S2']],
        names=['time', 'sensor_id']
    )
)

df_from_array = df_from_array.reset_index()
print("\nDataFrame from 3D NumPy array (using ravel):")
print(df_from_array)