def is_palindrome(str):
    """Returns TRUE if str is palindrome and FALSE otherwise."""
    if (str == str[::-1]):
        return True
    else:
        return False


print(is_palindrome(""))
print(is_palindrome("1"))
print(is_palindrome("2hyuuyh2"))
print(is_palindrome("RACEcar"))
print(is_palindrome("RACECAR"))