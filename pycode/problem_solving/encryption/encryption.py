#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    # Write your code here
    s = s.replace(' ', '')
    slen = math.sqrt(len(s))
    nrow, ncol = [math.floor(slen), math.ceil(slen)]
    v = [ "".join(s[k:len(s):ncol])for k in range(ncol) ]
    return " ".join(v)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    # s = 'have a nice day'
    s = 'chillout'
    result = encryption(s)
    print(result)

    # fptr.write(result + '\n')
    # fptr.close()
