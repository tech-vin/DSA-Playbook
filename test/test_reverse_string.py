import pytest
from src.array_revstring import *

def test_normal_string():
    assert reverseString('abc') == 'cba'
    assert reverseString('Let the game begin!') == '!nigeb emag eht teL'

    assert reverseStringUsingBuiltIn('abc') == 'cba'
    assert reverseStringUsingBuiltIn('Let the game begin!') == '!nigeb emag eht teL'

    assert reverseStringUsingTwoPointer('abc') == 'cba'
    assert reverseStringUsingTwoPointer('Let the game begin!') == '!nigeb emag eht teL'
