def is_prime(n):
    """Returns TRUE if n is prime and FALSE otherwise."""
    if (n < 0):
        return False
    if (n == 0 or n == 1):
        return False
    for i in range(2, (n//2)+1):
        if (n % i) == 0:
            return False
    return True


print(is_prime(1))
print(is_prime(-2))
print(is_prime(5))
print(is_prime(6))
print(is_prime(472882049))