import numpy as np

# This code flattens a 2D NumPy array into a 1D array

array = np.array([[1, 2, 3], [4, 5, 6]])  # np.array creates a NumPy array

flattened_array = array.flatten()  # flatten converts the 2D array into a 1D array

print(flattened_array)  # print displays the flattened array

# Output: [1 2 3 4 5 6]
