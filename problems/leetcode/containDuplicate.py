# https://leetcode.com/problems/contains-duplicate/description/

# using Dictionary -> O(n), O(n)
def containDuplicatesUsingDict(arr):
    '''
    Returns True if duplicate is found, otherwise returns False
    '''
    num_count = {}
    for item in arr:
        if item in num_count:
            return True
        else:
            num_count[item] = False
    return False


# using sets -> O(n), O(n)
def containDuplicatesUsingSet(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

# Easy, concise, !interview friedly -> O(n), O(n)
def containsDuplicateEasyWay(arr):
    return len(set(arr)) != len(arr)


testcases = [[1,2,3,1], [1,2,3,4], [1,1,1,3,3,4,3,2,4,2]]
print([containDuplicatesUsingDict(x) for x in testcases])
print([containDuplicatesUsingSet(x) for x in testcases])
print([containsDuplicateEasyWay(x) for x in testcases])
