from main import is_palindrome

def test_is_palindrome_happy():
    assert is_palindrome("wow")==True

def test_is_palindrome_unhappy():
    assert is_palindrome("favour")==False