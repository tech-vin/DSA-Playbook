import pytest
from problems.leetcode.rotateArray import rotateArrayInPlace

def test_rotate_normal():
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    expecting = [5, 6, 7, 1, 2, 3, 4]
    rotateArrayInPlace(arr, k)
    assert arr == expecting

def test_negative_mixed():
    arr = [-1, 0, 6, -4, 8, -7]
    k = 4
    expecting = [6, -4, 8, -7, -1, 0]
    rotateArrayInPlace(arr, k)
    assert arr == expecting

def test_multiple_rotates():
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 20
    expecting = [2, 3, 4, 5, 6, 7, 1]
    rotateArrayInPlace(arr, k)
    assert arr == expecting
