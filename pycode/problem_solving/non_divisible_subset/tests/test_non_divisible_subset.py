import pytest
from non_divisible_subset import nonDivisibleSubset

def test_case_01():
    lst = [19, 10, 12, 24, 25, 22]
    k = 4
    assert nonDivisibleSubset(k, lst) == 3

def test_case_02():
    lst = [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436]
    k = 7
    assert nonDivisibleSubset(k, lst) == 11

@pytest.mark.skip()
def test_case_03():
    lst = [2]
    k = 1
    assert nonDivisibleSubset(k, lst) == 1

@pytest.mark.skip()
def test_case_04():
    lst = [2, 5]
    k = 1
    assert nonDivisibleSubset(k, lst) == 1