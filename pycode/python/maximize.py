import itertools
import sys, math

K, M = input().rstrip().split()
K = int(K)
M = int(M)

sq = lambda x: x*x

arr = []
ni = []
for _ in range(K):
    lst = [ sq(int(x)) for x in input().rstrip().split()][1:]
    arr.append(lst)
    ni.append(len(lst))

v = max([ sum(tup) % M for tup in itertools.product(*arr) ])
print(v)
