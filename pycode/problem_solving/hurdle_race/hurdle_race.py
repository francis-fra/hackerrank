#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#

def hurdleRace(k, height):
    old_k = k
    for h in height:
        k += max(h - k, 0)
    return (k - old_k)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # first_multiple_input = input().rstrip().split()

    # n = int(first_multiple_input[0])
    # k = int(first_multiple_input[1])
    # height = list(map(int, input().rstrip().split()))
    n, k = [5, 4]
    height = [1, 6, 3, 5, 2]

    result = hurdleRace(k, height)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()