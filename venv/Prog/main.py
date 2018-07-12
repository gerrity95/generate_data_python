import matplotlib.pyplot as plt

from Include.random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walks()

plt.scatter(rw.x_values, rw.y_values, s=15)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.show()