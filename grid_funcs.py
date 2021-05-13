import numpy as np


ON = 255
OFF = 0
vals = [ON, OFF]


def random_grid(n):
    return np.random.choice(vals, n * n, p=[0.2, 0.8]).reshape(n, n)


def add_glider(i, j, grid):
    glider = np.array( [[0, 0, 255],
                        [255, 0, 255],
                        [0, 255, 255]])
    grid[i: i + 3, j: j + 3] = glider


def add_block(i, j, grid):
    block = np.array( [[255, 255],
                       [255, 255]])
    grid[i:i+2, j:j+2] = block


def add_loaf(i, j, grid):
    loaf = np.array([[0, 0, 0, 0],
                      [0, 255, 255, 0],
                      [0, 255, 0, 255],
                      [0, 0, 255, 0]])
    grid[i: i + 4, j: j + 4] = loaf


def add_gosper_gun(i, j, grid):
    gosper_gun = \
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0,
          255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 255, 255,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 0, 255, 255,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255],
         [255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 255, 0, 0, 0, 255,
          255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 255, 0, 255, 255, 0, 0, 0,
          0, 255, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0,
          255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 0, 0, 0, 255, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 255, 255, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    grid[i: i + 9, j: j + 36] = gosper_gun


def update(frame_num, img, org_grid, N):
    new_grid = org_grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((org_grid[i, (j - 1) % N] + org_grid[i, (j + 1) % N] +
                         org_grid[(i - 1) % N, (j - 1) % N] + org_grid[(i - 1) % N, (j + 1) % N] +
                         org_grid[(i + 1) % N, (j - 1) % N] + org_grid[(i + 1) % N, (j + 1) % N] +
                         org_grid[(i - 1) % N, j] + org_grid[(i + 1) % N, j]) / 255)

            if org_grid[i, j] == ON:
                if total < 2 or total > 3:
                    new_grid[i, j] = OFF
            elif total == 3:
                new_grid[i, j] = ON

    img.set_data(new_grid)
    org_grid[:] = new_grid[:]
    return img
