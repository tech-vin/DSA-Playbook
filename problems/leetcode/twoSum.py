# https://leetcode.com/problems/two-sum/description/

def twoSum(nums, target):
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
