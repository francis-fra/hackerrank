#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#
word_dict = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'quarter',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'half',
}

def next_hour(h):
    return h % 12 + 1

def format_minute(m):
    if m not in word_dict:
        minute = word_dict[20] + " " + word_dict[m-20]
    else:
        minute = word_dict[m]
    if m == 1:
        minute = minute + " " + "minute"
    elif m == 30 or m == 15:
        pass
    else:
        minute = minute + " " + "minutes"
    return minute

def timeInWords(h, m):
    # Write your code here
    result = "{minute} {adj} {hour}"
    if m == 0:
        return "{} o' clock".format(word_dict[h])
    elif m <= 30:
        adj = 'past'
        hour = word_dict[h]
        minute = format_minute(m)
        return result.format(minute=minute, adj=adj, hour=hour)
    elif m > 30:
        adj = 'to'
        hour = word_dict[next_hour(h)]
        minute = format_minute(60-m)
        return result.format(minute=minute, adj=adj, hour=hour)
    else:
        return "Impossible time"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # h = int(input().strip())
    # m = int(input().strip())
    h = 12
    m = 33

    result = timeInWords(h, m)
    print(result)

    # fptr.write(result + '\n')
    # fptr.close()
