from main import is_palindrome

def test_is_palindrome_happy():
    assert is_palindrome("wow")==True
    assert is_palindrome(545)==True
    assert is_palindrome(121)==True
    assert is_palindrome("did")==True
    assert is_palindrome("racecar")==True
    assert is_palindrome("radar")==True
    assert is_palindrome(5555555)==True

def test_is_palindrome_unhappy():
    assert is_palindrome("favour")==False
    assert is_palindrome("orange")==False
    assert is_palindrome("346")==False
    assert is_palindrome("Hello")==False