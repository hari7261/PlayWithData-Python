import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

plt.plot(x, y)
plt.title('Plot with Arrows')

# Add arrows
plt.annotate('Start', xy=(0, 0), xytext=(1, 1),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate('End', xy=(5, 25), xytext=(4, 20),
             arrowprops=dict(facecolor='red', shrink=0.05))

plt.show()
