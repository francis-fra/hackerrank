#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def make_rank_array(ranked):
    rank_position = ranked.copy()
    rank_position[0] = 1
    prev_score = ranked[0]
    prev_rank = 1
    for idx, score in enumerate(ranked[1:]):
        # start with 2nd item
        idx = idx + 1
        if prev_score > score:
            prev_rank = prev_rank + 1
        rank_position[idx] = prev_rank
        prev_score = score
    return rank_position

def climbingLeaderboard(ranked, player):
    # ranked is in descending order
    # player is in ascending order
    rank_position = make_rank_array(ranked)
    result = []

    # access from the back
    idx = len(ranked) - 1
    offset = 0
    for score in player:
        found = False
        while(idx >= 0):
            if score > ranked[idx]:
                idx -= 1
                continue
            elif score < ranked[idx]:
                result.append(rank_position[idx]+1)
                found = True
                break
            else:
                result.append(rank_position[idx])
                found = True
                break
        if found == False:
            result.append(1)
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    with open('./data/input.txt', 'r') as sys.stdin:

        # rank size
        ranked_count = int(input().strip())
        ranked = list(map(int, input().rstrip().split()))
        # num games
        player_count = int(input().strip())
        player = list(map(int, input().rstrip().split()))
        # 
        result = climbingLeaderboard(ranked, player)
        print(result)

        # fptr.write('\n'.join(map(str, result)))
        # fptr.write('\n')

        # fptr.close()