import numpy as np 

delft_chunk_size = 12

max_chunk_depth = 120

delft_chunk_thickness = np.array([2,3,4,6,8,10,12,15,12,10,10,8])/100

delft_depth_array = max_chunk_depth*delft_chunk_thickness

print(f"{delft_depth_array}\n{np.sum(delft_depth_array)}")

