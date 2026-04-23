import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

plt.plot(x, y, color='blue', linestyle='--', marker='o')

plt.title("Line Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.grid(True)

plt.show()