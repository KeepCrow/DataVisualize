from matplotlib import pyplot as plt

values = range(1, 1001)
squares = [n * n for n in values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(values, squares, c=squares, cmap=plt.cm.Blues, s=10)
ax.set_title('Scatter Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of Value', fontsize=14)
ax.axis([0, 1100, 0, 1_100_000])

# 设置刻度标记样式
ax.tick_params(labelsize=14)

plt.savefig('scatter_squares.png', bbox_inches='tight')
plt.show()