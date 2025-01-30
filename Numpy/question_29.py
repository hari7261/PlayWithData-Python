import numpy as np

# Transpose a 3D NumPy array
array = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
                  [[10, 11, 12], [13, 14, 15], [16, 17, 18]], 
                  [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])

transposed_array = np.transpose(array)

# Print the transposed array
print(transposed_array)
