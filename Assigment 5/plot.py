import matplotlib.pyplot as plt

# Data
epochs = list(range(1, 21))
accuracies = [
    87.83, 92.3, 93.67, 94.31, 94.91, 95.22, 95.5, 95.68, 95.83, 96.06,
    96.17, 96.35, 96.47, 96.66, 96.81, 96.81, 96.96, 97.17, 96.94, 97.24
]

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(epochs, accuracies, marker='o', linestyle='-', color='b')
plt.xlabel("Epoch")
plt.ylabel("Accuracy (%)")
plt.title("Training Accuracy vs. Epochs")
plt.grid(True)
plt.show()
