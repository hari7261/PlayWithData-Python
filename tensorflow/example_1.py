import tensorflow as tf
import numpy as np

# Create a TensorFlow constant
tensor = tf.constant([[1, 2], [3, 4]])

# Perform a basic operation: matrix multiplication
result = tf.matmul(tensor, tensor)

# Print the result
print("TensorFlow constant:")
print(tensor.numpy())
print("\nResult of matrix multiplication:")
print(result.numpy())
