original_array = [[2, 3, 1], [1], [], [1214]]
flat_list = [1, 2, 3, 4, 5, 6, 7, 8]

import numpy as np

result_array = []
test1 = np.array([1,3,4,5,6,7,7,1,3,1,5,4])
test2 = np.array([])
index = 0

for sublist in original_array:
    # print(sublist)
    new_sublist = []
    for element in sublist:
        
        if index < len(flat_list):
            new_sublist.append(flat_list[index])
            index += 1
    result_array.append(new_sublist)

print(np.reshape(test1, (2,3,2)))