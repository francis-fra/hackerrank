#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def is_csc_dsc_seq(arr, indices):
    "check if the violated indices are consecutive and in descending order"
    if (len(indices) == 1):
        return True
    else:
        prev_idx = indices[0]
        prev = arr[prev_idx]
        for idx in indices[1:]:
            if (arr[idx] > arr[prev_idx]):
                return False
            if (idx - 1 != prev_idx):
                return False
            prev_idx = idx
            prev = arr[prev_idx]
        return True

def is_dsc_seq(arr, indices):
    "check if the violated indices are in descending order"
    if (len(indices) == 1):
        return True
    else:
        prev_idx = indices[0]
        prev = arr[prev_idx]
        for idx in indices[1:]:
            if (arr[idx] > arr[prev_idx]):
                return False
            prev_idx = idx
            prev = arr[prev_idx]
        return True

def is_boundary_asc(arr, indices):
    "check if ascending if after swapped"
    arrlen = len(arr)
    back_idx = indices[-1]
    front_idx = indices[0]
    # check front
    if front_idx >= 2 and arr[back_idx] < arr[front_idx-2]:
        return False
    # check back
    if (back_idx + 1 < arrlen) and (arr[front_idx-1] > arr[back_idx+1]):
        return False
    return True 

def almostSorted(arr):
    # find violation
    violation_index = []
    for idx, v in enumerate(arr[1:]):
        # fix index
        idx = idx + 1
        if arr[idx] < arr[idx-1]:
            violation_index.append(idx)
    if len(violation_index) == 0:
        print("yes")
        return (violation_index)
    # check if swap ok
    if len(violation_index) <= 2:
        if (is_dsc_seq(arr, violation_index)) and is_boundary_asc(arr, violation_index):
            print("yes")
            # for reporting add 1 to index
            print("swap {} {}".format(violation_index[0], violation_index[-1]+1))
            return (violation_index)
    # check if reverse ok
    if (is_csc_dsc_seq(arr, violation_index)) and is_boundary_asc(arr, violation_index):
        print("yes")
        # for reporting add 1 to index
        print("reverse {} {}".format(violation_index[0], violation_index[-1]+1))
    else:
        print("no")
    return (violation_index)

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    violation_index = almostSorted(arr)
    print(violation_index)

