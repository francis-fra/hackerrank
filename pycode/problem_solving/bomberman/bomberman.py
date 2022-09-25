#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

# 0. init
# 1. wait
# 2. fill all
# 3. wait (bomb)
# 4. fill all
# 5. wait

max_time = 3

def show_grid(grid):
    for row in grid:
        print(row)

def make_num_grid(grid):
    nrow = len(grid)
    ncol = len(grid[0])
    num_grid = []
    for _ in range(nrow):
        num_grid.append([-1] * ncol)
    for i, row in enumerate(grid):
        for j, item in enumerate(row):
            if (item == 'O'):
                num_grid[i][j] = max_time
    return num_grid

def make_string_grid(num_grid):
    nrow = len(num_grid)
    ncol = len(num_grid[0])
    grid = []
    for _ in range(nrow):
        grid.append(['.'] * ncol)
    for i, row in enumerate(num_grid):
        for j, item in enumerate(row):
            if (item >= 0):
                grid[i][j] = 'O' 
    grid = map(lambda x: "".join(x), grid)
    return list(grid)

def bomb(num_grid, zero_pos, empty_pos):
    nrow = len(num_grid)
    ncol = len(num_grid[0])
    # clear 
    for r, c in zero_pos:
        # top
        if r-1 >= 0:
            num_grid[r-1][c] = -1
            empty_pos.add((r-1, c))
        # down 
        if r+1 < nrow:
            num_grid[r+1][c] = -1
            empty_pos.add((r+1, c))
        # left
        if c-1 >= 0:
            num_grid[r][c-1] = -1
            empty_pos.add((r, c-1))
        # right 
        if c+1 < ncol:
            num_grid[r][c+1] = -1
            empty_pos.add((r, c+1))
        # center
        num_grid[r][c] = -1
        empty_pos.add((r, c))
    return empty_pos

# FIXME: memorize fill bomb
def count_down(num_grid):
    nrow = len(num_grid)
    ncol = len(num_grid[0])
    zero_pos = []
    for k in range(nrow):
        for j in range(ncol):
            if num_grid[k][j] > -1:
                num_grid[k][j] -= 1
            if num_grid[k][j] == 0:
                zero_pos.append((k, j))
    return zero_pos        

def fill_bomb(num_grid, empty_pos):
    for k, j in empty_pos:
        num_grid[k][j] = max_time

def make_empty_pos(num_grid):
    nrow = len(num_grid)
    ncol = len(num_grid[0])
    empty_pos = set()
    for k in range(nrow):
        for j in range(ncol):
            if num_grid[k][j] == -1:
                empty_pos.add((k, j))
    return empty_pos

def bomberMan(n, grid):
    # Write your code here
    num_grid = make_num_grid(grid)
    empty_pos = make_empty_pos(num_grid)
    for t in range(1, n+1):
        # print('------------------------------------------------------------')
        # print(t)
        zero_pos = count_down(num_grid)
        # print(zero_pos)
        empty_pos = bomb(num_grid, zero_pos, empty_pos)
        # print(empty_pos)
        if t % 2 == 0:
            fill_bomb(num_grid, empty_pos)
            empty_pos = set()
        # DEBUG
        # grid = make_string_grid(num_grid)
        # show_grid(grid)
        # print(num_grid)
    grid = make_string_grid(num_grid)
    return grid

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    # dimension
    r = int(first_multiple_input[0])
    c = int(first_multiple_input[1])
    # seconds to simulate
    n = int(first_multiple_input[2])
    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)
    show_grid(result)
        

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()

# lst = [(1,2), (3, 4), (1, 2)]
# set(lst)
# for x, y in set(lst):
#     print(x, y)