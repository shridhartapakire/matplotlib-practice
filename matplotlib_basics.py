import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Plot
plt.plot(x, y, color='blue', linestyle='--', marker='o')

# Title and labels
plt.title("Sample Line Graph")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Grid
plt.grid(True)

# Show graph
plt.show()
