import numpy as np

# Flatten a 3D NumPy array into a 1D array
array = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
                  [[10, 11, 12], [13, 14, 15], [16, 17, 18]], 
                  [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])

flattened_array = array.flatten()

# Print the flattened array
print(flattened_array)
