# https://leetcode.com/problems/move-zeroes/

def moveZeros(arr):
    '''
    Move all the zeros to the end, while maintaining non-zero number order.
    
    Example:
        if the given arr is [0, 1, 2, 0, 3] then output will be:
        [1, 2, 3, 0, 0]
    Args:
        arr [list] - array of numbers

    '''
    i = 0
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1

arr = [[0, 1, 0, 2], [0, 1, 2], [0], [], [0, -1, -2, 0, -5, 4, 1]]
[moveZeros(x) for x in arr]
print([x for x in arr])