import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Simulated data for a machine learning model's performance
y_true = np.array([0, 1, 0, 1, 0, 1, 0, 1, 0, 1])
y_pred = np.array([0, 0, 0, 1, 0, 1, 0, 1, 1, 1])

# Create a confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Create a custom visualization for the confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix for Model Performance')
plt.show()
