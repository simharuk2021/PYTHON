import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
# make a random walk
    rw=RandomWalk(50_000)
    rw.fill_walk()
    # plot the points in the walk

    plt.style.use('classic')
    # show full screen
    fig, ax=plt.subplots(figsize=(15, 9))
    
    # color the points 
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
    
    # Emphasise the first and last points
    
    ax.scatter(0,0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c = 'red', edgecolors='none', s=100)
    
    # remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()
    keep_running = input("Press y to Make another random walk, or anything else to quit: ")
    if keep_running != 'y':
        print("Walk ended")
        break
