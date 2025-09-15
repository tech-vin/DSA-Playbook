import pytest
from problems.leetcode.containDuplicate import containDuplicatesUsingSet

def test_normal_duplicates():
    assert containDuplicatesUsingSet([1, 2, 3, 1]) == True

def test_negative_duplicates():
    assert containDuplicatesUsingSet([-1, 2, 3 -1]) == True

def test_no_duplicates():
    assert containDuplicatesUsingSet([1, 2, 3]) == False

def test_empty_array():
    assert containDuplicatesUsingSet([]) == False

def test_all_zeros():
    assert containDuplicatesUsingSet([0, 0, 0, 0]) == True