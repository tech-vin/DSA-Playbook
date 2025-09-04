def sanityAndDocString(string):
    '''
    Returns reversed string
    
    Example:
        If string is 'Let the game begin!' then output will be:
        '!nigeb emag eht teL'
    Args:
        s (str) : A word or sentence
    '''
    if not isinstance(string, str):
        raise TypeError("reverseString expects a str" )
    
    if len(string) <= 1:
        return string

# Reverse the given string
# below is a naive solution with O(n^2)
def reverseString(string):
    sanityAndDocString(string)
    output = ''
    for ch in string:
        output = ch + output
        
    return output

# below is optimized solution with O(n) using two-pointer shows mechanics
def reverseStringUsingTwoPointer(string):
    sanityAndDocString(string)
    chars = list(string)
    print("value of char: ",chars)
    i, j = 0, len(chars) - 1
    while i < j:
        chars[i], chars[j] = chars[j], chars[i]
        i += 1
        j -= 1
    return ''.join(chars)



# another optimized way with O(n) using pythonic way
def reverseStringUsingBuiltIn(string):
    sanityAndDocString(string)
    
    return string[::-1]


testcases = ['Let the game begin!', '', 'V']
print([reverseString(x) for x in testcases])
print([reverseStringUsingBuiltIn(x) for x in testcases])
print([reverseStringUsingTwoPointer(x) for x in testcases])
