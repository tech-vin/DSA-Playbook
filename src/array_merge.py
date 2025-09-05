def mergeArrayUsingHeapq(arr1, arr2):
    '''
    Merge two Sorted Arrays such that it remains sorted

    Example:
        If two arrays are such that:
        arr1 = [1, 3, 5, 7]
        arr2 = [2, 3, 4, 6, 8]
        
        then output will be:
        [1, 2, 3, 3, 4, 5, 6, 7, 8]

    Args:
        arr [list] : two sorted arrays
    '''
    import heapq
    return list(heapq.merge(arr1, arr2))
    
def mergeArrayUsingTwoPointer(arr1, arr2):
    '''
    Merge two sorted arrays such that it remains sorted

    Example:
        if two sorted arrays are such that:
        arr1 = [1, 3, 5, 7, 9]
        arr2 = [2, 4, 6, 8]

        then output will be :
        [1, 2, 3, 4, 5, 6, 7, 8, 9]

    Args:
        arr [list] : two sorted arrays
    '''

    i, j = 0, 0
    merged = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    '''
    # same as code in line 57, 58
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    '''
    # more pythonic way
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])

    return merged



arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 9, 10]

print("Heapq: ", mergeArrayUsingHeapq(arr1, arr2))
print("Two Pointer: ", mergeArrayUsingTwoPointer(arr1, arr2))