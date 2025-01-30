import numpy as np

# Concatenate three NumPy arrays horizontally
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
array3 = np.array([[9, 10], [11, 12]])

concatenated_array = np.hstack((array1, array2, array3))

# Print the concatenated array
print(concatenated_array)
