import grid_funcs
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import argparse


def CMI():
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation")

    parser.add_argument('--grid-size', dest='n', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    return parser.parse_args()


def main():
    args = CMI()

    n = 100                                        # set grid size
    if args.n and int(args.n) > 8:
        n = int(args.n)

    update_interval = 50                            # set animation update interval
    if args.interval:
        update_interval = int(args.interval)

    grid = np.array([])                             # declare grid
    if args.glider:
        grid = np.zeros(n * n).reshape(n, n)
        grid_funcs.add_glider(1, 1, grid)
    elif args.gosper:
        grid = np.zeros(n * n).reshape(n, n)
        grid_funcs.add_gosper_gun(1, 1, grid)
    else:
        grid = grid_funcs.random_grid(n)

    # set up animation

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest', cmap=plt.cm.Greys)
    ani = animation.FuncAnimation(fig, grid_funcs.update, fargs=(img,grid, n, ), frames=10,
                                  interval=update_interval, save_count=50)

    if args.movfile:
        ani.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])

    plt.show()


if __name__ == '__main__':
    main()