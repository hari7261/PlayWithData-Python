import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
x_data = np.linspace(-1, 1, 100)
y_data = x_data * 2 + np.random.randn(*x_data.shape) * 0.3

# Create a simple neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])

# Compile the model
model.compile(optimizer='sgd', loss='mse')

# Train the model
history = model.fit(x_data, y_data, epochs=100, verbose=0)

# Plot the training loss
plt.plot(history.history['loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.show()

# Make predictions
y_pred = model.predict(x_data)

# Plot the data and the model's predictions
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, y_pred, color='red', label='Model Prediction')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Data and Model Prediction')
plt.legend()
plt.show()
