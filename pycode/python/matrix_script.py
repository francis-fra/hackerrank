#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

s = "".join([ "".join([wrd[idx] for wrd in matrix]) for idx in range(m)])
regex_code = r"[a-zA-Z0-9]([^a-zA-Z0-9]+\s?)[a-zA-Z0-9]"
regex_code = r"([a-zA-Z0-9])([^a-zA-Z0-9]+\s?)([a-zA-Z0-9])"
regex_replace = r"\1 \3"
print(re.sub(regex_code, regex_replace, s))

