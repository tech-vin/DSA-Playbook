import pytest
from src.array_revstring import *

def test_normal_string():
    assert reverseString('abc') == 'cba'
    assert reverseString('Let the game begin!') == '!nigeb emag eht teL'

    assert reverseStringUsingBuiltIn('abc') == 'cba'
    assert reverseStringUsingBuiltIn('Let the game begin!') == '!nigeb emag eht teL'

    assert reverseStringUsingTwoPointer('abc') == 'cba'
    assert reverseStringUsingTwoPointer('Let the game begin!') == '!nigeb emag eht teL'

def test_empty_string():
    assert reverseString('') == ''
    assert reverseStringUsingBuiltIn('') == ''
    assert reverseStringUsingTwoPointer('') == ''

def test_valid_input():
    with pytest.raises(TypeError):
        reverseString(1234)
    with pytest.raises(TypeError):
        reverseString(True)
    with pytest.raises(TypeError):
        reverseString(['a', 'b'])

    with pytest.raises(TypeError):
        reverseStringUsingBuiltIn(1234)
    with pytest.raises(TypeError):
        reverseStringUsingBuiltIn(True)
    with pytest.raises(TypeError):
        reverseStringUsingBuiltIn(['a', 'b'])

    with pytest.raises(TypeError):
        reverseStringUsingTwoPointer(1234)
    with pytest.raises(TypeError):
        reverseStringUsingTwoPointer(True)
    with pytest.raises(TypeError):
        reverseStringUsingTwoPointer(['a', 'b'])

def test_single_char():
    assert reverseString('V') == 'V'
    assert reverseStringUsingBuiltIn('V') == 'V'
    assert reverseStringUsingTwoPointer('V') == 'V'

def test_special_char():
    assert reverseString('#$@!') == '!@$#'
    assert reverseStringUsingTwoPointer('#$@!') == '!@$#'
    assert reverseStringUsingBuiltIn('#$@!') == '!@$#'


    