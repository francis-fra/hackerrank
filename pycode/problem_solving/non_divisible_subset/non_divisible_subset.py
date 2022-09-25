# https://www.hackerrank.com/challenges/non-divisible-subset

from __future__ import annotations
from collections import Counter

def nonDivisibleSubset(k:int , s: list[int]) -> int:
    c = Counter([ss % k for ss in s])
    n = sum(max(c[i], c[k-i]) for i in range(1, k//2 + k%2))
    return n + (0 in c) + (k%2 == 0 and k/2 in c)

# def get_solution(lst, divisible_pairs, max_so_far):
#     "search by tree"
#     if len(lst) < max_so_far:
#         return max_so_far
#     print(f"lst: {lst}, pairs: {divisible_pairs}")
#     if (len(divisible_pairs) == 0):
#         print(lst)
#         return len(lst)
#     else:
#         x, y = divisible_pairs.pop()
#         # check if x and are both in lst
#         if (x in lst) and (y in lst):
#             lst01 = lst.copy()
#             lst01.remove(x)
#             lst02 = lst.copy()
#             lst02.remove(y)
#             ans01 = get_solution(lst01, divisible_pairs.copy(), max_so_far)
#             max_so_far = max(ans01, max_so_far)
#             ans02 = get_solution(lst02, divisible_pairs.copy(), max_so_far)
#             max_so_far = max(ans02, max_so_far)
#             return max_so_far
#         else:
#             return get_solution(lst, divisible_pairs.copy(), max_so_far)

# def nonDivisibleSubset(k: int, s: list[int]) -> int:
#     divisible_pairs = get_divisible_pairs(s, k)
#     print(len(divisible_pairs))
#     return get_solution(s, divisible_pairs, 0)

# def get_divisible_pairs(s: list[int], k) -> list[int]:
#     return [(x, y) for (x, y) in itertools.combinations(s, 2) if (x+y) % k == 0]
