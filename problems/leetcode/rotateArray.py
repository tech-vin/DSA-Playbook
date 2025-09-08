# https://leetcode.com/problems/rotate-array/description/

def rotateArray(arr, k):  # n(n^2) - naive solution
    '''
    Rotate the array to the right by k steps

    Example:
        If the given array is [1,2,3,4,5,6,7] and k = 3, then the output will be:
        [5,6,7,1,2,3,4]

    Args:
        arr [list] - list of numbers
        k [int] - number of steps
    '''
    for _ in range(k):
        arr.insert(0, arr.pop())
    
    return arr

def rotateArrayInPlace(arr, k):
    '''
    Rotate the array to the right by k steps

    Example:
        If the given array is [1,2,3,4,5,6,7] and k = 3, then the output will be:
        [5,6,7,1,2,3,4]

    Args:
        arr [list] - list of numbers
        k [int] - number of steps
    '''
    n = len(arr)
    k %= n

    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)



nums = [1,2,3,4,5,6,7]
k = 3
rotateArrayInPlace(nums, k)
print(nums)