import numpy as np

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

concatenated_array = np.concatenate((array1, array2), axis=1)

print(concatenated_array)

# Output:
# [[1 2 5 6]
#  [3 4 7 8]]
