# https://leetcode.com/problems/rotate-array/description/

nums = [1,2,3,4,5,6,7]
k = 3

l = len(nums)
print(l)
compliment = l - k
print(compliment)
print(nums[compliment:])