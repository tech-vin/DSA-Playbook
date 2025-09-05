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
✅ Large input (stress test)
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
    arr1, arr2, expected = [1, 2, 3], [4, 1], [1, 1, 2, 3, 4]
    assert mergeArrayUsingHeapq(arr1, arr2, expected)

def test_negative_numbers():
    arr1, arr2, expected = [-1, -5, -2]

def test_mixed_negative_positive():
    pass

def test_single_element():
    pass

def test_large_input():
    pass