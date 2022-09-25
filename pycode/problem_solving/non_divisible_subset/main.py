import sys
from non_divisible_subset import nonDivisibleSubset

def test_case_00():
    with open('./data/input.txt', 'r') as sys.stdin:
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])
        # print(n, k)
        s = list(map(int, input().rstrip().split()))
        result = nonDivisibleSubset(k, s)
        print(result)

def test_case_01():
    lst = [19, 10, 12, 24, 25, 22]
    k = 4
    ans = nonDivisibleSubset(k, lst)
    print(ans)

def test_case_02():
    lst = [1, 7, 2, 4]
    k = 3
    ans = nonDivisibleSubset(k, lst)
    print(ans)

def test_case_03():
    lst = [1, 7, 2, 4]
    lst01 = lst.copy()
    lst01.remove(1)
    lst02 = lst.copy()
    lst02.remove(7)
    print(lst01)
    print(lst02)

def test_case_04():
    lst = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
    k = 7
    ans = nonDivisibleSubset(k, lst)
    print(ans)

def main():
    test_case_00()
    # test_case_01()
    # test_case_02()
    # test_case_03()
    # test_case_04()


main()