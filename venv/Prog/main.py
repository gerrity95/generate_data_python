import matplotlib.pyplot as plt

from Include.random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walks()

plt.figure(figsize=(10,6))

while True:
    plt.scatter(rw.x_values, rw.y_values, s=15)

    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=14)
    plt.ylabel("Square of Value", fontsize=14)

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    plt.scatter(0, 0, c='green', edgecolors='none', s=30)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=30)

    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y/n)')

    if keep_running == 'n':
        break