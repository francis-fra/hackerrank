import numpy

def numpy_stat(arr):
    print(numpy.mean(arr, axis = 1))
    print(numpy.var(arr, axis = 0))
    print(numpy.std(arr))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    # size
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    M = [ [ float(x) for x in input().rstrip().split()] for idx in range(n)]
    print(M)
    # s = list(map(int, input().rstrip().split()))
    numpy_stat(M)