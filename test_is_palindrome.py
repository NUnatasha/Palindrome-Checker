from main import is_palindrome

def test_is_palindrome_happy():
    assert is_palindrome("wow")==True
    assert is_palindrome(545)==True

def test_is_palindrome_unhappy():
    assert is_palindrome("favour")==False