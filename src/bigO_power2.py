# BIG O -> O(n^2)
# when two loops are executed inside the function there complexities are added.
# eg -> loop1 --> 10 and loop2 --> 20, there complexities will be added and become O(2n) which is equivalent to O(n)
# but when loops are nested then instead of addition we do multiplication and the complexity becomes O(n^2)

def letterCombination(arr):
    '''
    Prints combination of letter

    Example:
        a a
        a b
        b a
        b b

    Args:
        arr (list) : array of letters
    '''
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])


arr = ['a', 'b', 'c']
print(letterCombination(arr))