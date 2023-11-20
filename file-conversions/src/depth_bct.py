import numpy as np

np_arr = [[22.77645264, 32.13683297, 39.33420747, 45.4304099, 50.77953391, 55.5634053, 213123, 64.0738571, 67.93541815, 71.62295253]]

nan_index = np.argwhere(np.isnan(np_arr[0]))

print(nan_index)