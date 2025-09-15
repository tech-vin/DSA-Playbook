# https://leetcode.com/problems/maximum-subarray/

def maxSubArrayOptimised(arr):
    '''
    Returns the sum of subarray with the largest sum.

    Example:
        If the given arr is [-2,1,-3,4,-1,2,1,-5,4] 
        then the output will be 6.
        
        The subarray [4,-1,2,1] has the largest sum 6.

    Args:
        arr [list] - list of numbers 
    '''
    maxSum = float('-inf')
    currentSum = 0
    
    for num in arr:
        currentSum += num

        if currentSum > maxSum:
            maxSum = currentSum

        if currentSum < 0:
            currentSum = 0
    
    return maxSum

def maxSubArray(arr):
    '''
    Returns the sum of subarray with the largest sum.

    Example:
        If the given arr is [-2,1,-3,4,-1,2,1,-5,4] 
        then the output will be 6.
        
        The subarray [4,-1,2,1] has the largest sum 6.

    Args:
        arr [list] - list of numbers 
    '''
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(current_sum, max_sum)
    
    return max_sum    


testcases  = [[-2,1,-3,4,-1,2,1,-5,4], [1], [5,4,-1,7,8]]
print([maxSubArray(x) for x in testcases])
print([maxSubArrayOptimised(x) for x in testcases])