import matplotlib.pyplot as plt

expenses = [100, 200, 150, 300, 250, 400, 350, 200, 150, 300]

plt.hist(expenses, bins=5)

plt.title("Expense Distribution")
plt.xlabel("Amount")
plt.ylabel("Frequency")

plt.show()