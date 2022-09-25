#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#

def left_3_shift(A, idx):
    first = A[idx]
    A[idx] = A[idx+1]
    A[idx+1] = A[idx+2]
    A[idx+2] = first

def find_value_idx(A, start_idx, target_value):
    # find position of target value
    for k in range(start_idx, len(A)):
        if A[k] == target_value:
            return k

def do_shift(A, idx):
    "shift until the value is at position idx"
    target_value = idx+1
    cur_idx = find_value_idx(A, idx, target_value)
    num_moves = cur_idx - idx
    for _ in range(num_moves):
        front_idx = max(idx, cur_idx-2)
        if front_idx >=  len(A) - 2:
            return False
        left_3_shift(A, front_idx)
        # print(front_idx, A)
        cur_idx -= 1
    return True


def larrysArray(A):
    end_idx = len(A) - 1
    cur_idx = 0
    # check if cur pos is fine
    while cur_idx < end_idx:
        if A[cur_idx] != cur_idx+1:
            is_success = do_shift(A, cur_idx)
            if is_success == False:
                return "NO"
        else:
            cur_idx += 1
    return "YES"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)
        print(result)

