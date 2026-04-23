import matplotlib.pyplot as plt

categories = ['Food', 'Travel', 'Shopping', 'Bills']
amounts = [500, 300, 700, 400]

plt.bar(categories, amounts, color='green')

plt.title("Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount")

plt.show()