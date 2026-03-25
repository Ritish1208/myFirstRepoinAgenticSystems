import numpy as np
import matplotlib.pyplot as plt

# 1. Create list of 10 epochs (1 to 10)
epochs = list(range(1, 11))

# 2. Generate synthetic training loss values using NumPy
np.random.seed(0)  # for consistent results
loss = np.random.uniform(0.5, 1.5, 10)

# 3A. Line Plot: Loss vs Epoch
plt.figure(figsize=(8, 5))
plt.plot(epochs, loss, marker='o')
plt.title("Loss vs Epoch")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# 3B. Scatter Plot: Epoch vs Loss
plt.figure(figsize=(8, 5))
plt.scatter(epochs, loss)
plt.title("Epoch vs Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.grid(True)
plt.show()

# 4. Bar Chart comparing accuracy of three models
models = ['Model A', 'Model B', 'Model C']
accuracy = [0.85, 0.90, 0.88]

plt.figure(figsize=(8, 5))
plt.bar(models, accuracy)
plt.title("Model Accuracy Comparison")
plt.xlabel("Models")
plt.ylabel("Accuracy")
plt.show()