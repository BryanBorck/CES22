def sum_to(n):
    """Returns the sum of integers up to n, including n."""
    sum_n = 0 
    for i in range(n):
        sum_n += (i+1)
    return sum_n


print(sum_to(1))
print(sum_to(3))
print(sum_to(10))
print(sum_to(200))