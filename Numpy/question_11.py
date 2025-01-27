import numpy as np

# This code reshapes a 1D NumPy array into a 2D array of shape (2, 5)

array = np.arange(1, 11)  # np.arange generates values from 1 to 10
reshaped_array = array.reshape(2, 5)  # reshape changes the shape of the array

print(reshaped_array)  # print displays the reshaped array

# Output:
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]
