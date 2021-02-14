import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 3, 100)
y = (x - 1) ** 2

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('zero')

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# plot the function
plt.plot(x, y, 'r')

# show the plot
plt.show()
