import numpy as np

array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

result = np.vstack((array1, array2))

print(result)

# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]
