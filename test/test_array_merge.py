import pytest
from src.array_merge import mergeArrayUsingHeapq
from src.array_merge import mergeArrayUsingTwoPointer

'''
# test senarios
✅ Normal case
✅ Empty input(s)
✅ No overlap
✅ Duplicate elements
✅ Unequal lengths
✅ Negative numbers
✅ Mixed numbers
✅ Single element
'''

def test_normal_case():
    arr1, arr2, expected = [1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]
    assert mergeArrayUsingHeapq(arr1, arr2) == expected
    assert mergeArrayUsingTwoPointer(arr1, arr2) == expected

def test_empty_inputs():
    arr1, arr2, expected = [], [], []
    assert mergeArrayUsingHeapq(arr1, arr2) == expected
    assert mergeArrayUsingTwoPointer(arr1, arr2) == expected

def test_no_overlap():
    arr1, arr2, expected = [1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]
    assert mergeArrayUsingHeapq(arr1, arr2) == expected
    assert mergeArrayUsingTwoPointer(arr1, arr2) == expected

def test_duplicate_elements():
    arr1, arr2, expected = [2, 2, 2], [2, 2, 2], [2, 2, 2, 2, 2, 2]
    assert mergeArrayUsingHeapq(arr1, arr2) == expected
    assert mergeArrayUsingTwoPointer(arr1, arr2) == expected

def test_unequal_elements():
    arr1, arr2, expected = [1, 2, 3], [4, 1], [1, 2, 3, 4, 1] # merge sorted array: we assume that arrays are already sorted
    assert mergeArrayUsingHeapq(arr1, arr2) == expected
    assert mergeArrayUsingTwoPointer(arr1, arr2) == expected

def test_negative_numbers():
    arr1, arr2, expected = [-5, -2, -1], [-10, -8, -5], [-10, -8, -5, -5, -2, -1]
    assert mergeArrayUsingHeapq(arr1, arr2) ==  expected
    assert mergeArrayUsingTwoPointer(arr1, arr2) == expected

def test_mixed_negative_positive():
    arr1, arr2, expected = [-8, 1, 2], [1, 5, 9], [-8, 1, 1, 2, 5, 9]
    assert mergeArrayUsingHeapq(arr1, arr2) == expected
    assert mergeArrayUsingTwoPointer(arr1, arr2) == expected

def test_single_element():
    assert mergeArrayUsingTwoPointer([1], [0]) == [0, 1]
    assert mergeArrayUsingHeapq([5], [-4]) == [-4, 5]