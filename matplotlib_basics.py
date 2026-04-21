import matplotlib.pyplot as plt

# -------- Line Plot --------
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.figure()
plt.plot(x, y, color='blue', linestyle='--', marker='o')
plt.title("Line Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)

plt.show()

# -------- Bar Chart --------
categories = ['Food', 'Travel', 'Shopping', 'Bills']
amounts = [500, 300, 700, 400]

plt.figure()
plt.bar(categories, amounts, color='green')
plt.title("Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount")

plt.show()

# -------- Scatter Plot --------

x_scatter = [1, 2, 3, 4, 5]
y_scatter = [5, 15, 20, 25, 30]

plt.figure()

plt.scatter(x_scatter, y_scatter, color='red')

plt.title("Scatter Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.show()

# -------- Subplots Example --------

import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y_line = [10, 20, 25, 30, 40]
y_bar = [5, 15, 20, 25, 30]

# Create subplots (1 row, 2 columns)
plt.figure(figsize=(10, 4))

# First subplot - Line
plt.subplot(1, 2, 1)
plt.plot(x, y_line, color='blue', marker='o')
plt.title("Line Plot")

# Second subplot - Bar
plt.subplot(1, 2, 2)
plt.bar(x, y_bar, color='orange')
plt.title("Bar Chart")

plt.tight_layout()
plt.show()