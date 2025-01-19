import numpy as np

array = np.array([1, -2, 3, -4, 5, -6, 7, -8, 9, -10])
array[array < 0] = 0

print(array)

# Output: [ 1  0  3  0  5  0  7  0  9  0]
