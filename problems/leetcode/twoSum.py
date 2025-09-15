# https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
    '''
    Returns indices of 2 numbers whose sum is equal to target

    Example:
        If the arr is [2, 7, 11, 15] and target is 9, then output will be:
        [0, 1] because 2 + 7 is 9 and 2 is present at index 0 and 7 at index 1.

    Args:
        nums [list] : list of array
        target [int] : integer value

    '''
    nums_dict = {}
    for indx, val in enumerate(nums):
        complement = target - val 
        if complement in nums_dict:
            return indx, nums_dict[complement]
        nums_dict[val] = indx
    return []

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))