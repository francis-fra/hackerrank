#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    # generae eight rays from queen position
    obstacles = [str(x) for x in obstacles]
    obstacles = set(obstacles)
    count = 0
    # down
    for offset in range(1, r_q): 
        cur = str([r_q - offset, c_q] )
        if (cur in obstacles):
            break
        count += 1

    # up
    for offset in range(1, n-r_q+1): 
        cur = str([r_q + offset, c_q] )
        if (cur in obstacles):
            break
        count += 1

    # left
    for offset in range(1, c_q): 
        cur = str([r_q, c_q - offset] )
        if (cur in obstacles):
            break
        count += 1

    # right 
    for offset in range(1, n-c_q+1): 
        cur = str([r_q, c_q + offset] )
        if (cur in obstacles):
            break
        count += 1

    # ne 
    mq = max(r_q, c_q)
    for offset in range(1, n-mq+1): 
        cur = str([r_q + offset, c_q + offset] )
        if (cur in obstacles):
            break
        print(cur)
        count += 1

    # sw 
    mq = min(r_q, c_q)
    for offset in range(1, mq): 
        cur = str([r_q - offset, c_q - offset] )
        if (cur in obstacles):
            break
        print(cur)
        count += 1

    # se 
    mq = min(r_q, n-c_q+1)
    for offset in range(1, mq): 
        cur = str([r_q - offset, c_q + offset] )
        if (cur in obstacles):
            break
        print(cur)
        count += 1

    # nw 
    mq = min(n-r_q+1, c_q)
    for offset in range(1, mq): 
        cur = str([r_q + offset, c_q - offset] )
        if (cur in obstacles):
            break
        print(cur)
        count += 1

    return count



if __name__ == '__main__':
    with open('./data/input.txt', 'r') as sys.stdin:

        first_multiple_input = input().rstrip().split()
        # board size
        n = int(first_multiple_input[0])
        # num obstacles
        k = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        # queen position
        r_q = int(second_multiple_input[0])
        c_q = int(second_multiple_input[1])

        obstacles = []

        # read obstables
        for _ in range(k):
            obstacles.append(list(map(int, input().rstrip().split())))

        # print(obstacles)

        result = queensAttack(n, k, r_q, c_q, obstacles)
        print(result)
