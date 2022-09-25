
if __name__ == '__main__':
    n, m = input().rstrip().split()

    arr = input().rstrip().split()
    A = set(input().rstrip().split())
    B = set(input().rstrip().split())
    res = 0
    for x in arr:
        if x in A:
            res += 1
        if x in B:
            res -= 1
    print(res)