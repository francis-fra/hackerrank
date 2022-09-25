#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#

legend = {
    'top': 1,
    'right': 2,
    'down': 3,
    'left': 4,
}

def get_opposite_direction(d):
    if d == 1:
        return 3
    elif d == 3:
        return 1
    elif d == 2:
        return 4
    else:
        return 2


def find_starting(M, nrow, ncol):
    for k in range(nrow):
        for j in range(ncol):
            if M[k][j] == 'M':
                return (k, j)

def find_possible_paths(M, nrow, ncol, cur):
    "return possible directions"
    paths = []
    destination = None
    x, y = cur
    # top
    if x-1 >= 0:
        if M[x-1][y] != 'X':
            paths.append(legend['top'])
            if M[x-1][y] == '*':
                destination = legend['top']
    # left
    if y-1 >= 0:
        if M[x][y-1] != 'X':
            paths.append(legend['left'])
            if M[x][y-1] == '*':
                destination = legend['left']
    # right
    if y+1 < ncol:
        if M[x][y+1] != 'X':
            paths.append(legend['right'])
            if M[x][y+1] == '*':
                destination = legend['right']
    # down 
    if x+1 < nrow:
        if M[x+1][y] != 'X':
            paths.append(legend['down'])
            if M[x+1][y] == '*':
                destination = legend['down']
    return (paths, destination)


def countLuck(matrix, k):
    # Write your code here
    num_intersection = 0
    stack = []
    nrow = len(matrix)
    ncol = len(matrix[0])
    cur = find_starting(matrix, nrow, ncol)
    cur_direction = None
    # FIXME: stack is emtpy only if the intersectio is newly found
    while True: 
        if len(stack) == 0:
            paths, destination = find_possible_paths(matrix, nrow, ncol, cur)
            # at intersection
            if len(paths) > 1:
                num_intersection += 1
                # TODO: insert opposite of current moving direction
                if cur_direction is not None:
                    # add cur direction last
                    opp_direction = get_opposite_direction(cur_direction)
                    # add paths to stack
                    for dir in paths:
                        if dir != opp_direction:
                            stack.apped(dir)
                    stack.append(opp_direction) 
                else:
                    for dir in paths:
                        if dir != opp_direction:
                            stack.apped(dir)
            else:
                if cur_direction is None:
                    cur_direction = paths[0]
                # continue with current direction
            if destination is not None:
                break
        else:
            pass
    return num_intersection



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])

        matrix = []
        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)

        # fptr.write(result + '\n')

    # fptr.close()
