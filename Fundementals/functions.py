def gcd(a, b):
    """
    Returns the greatest common divider of a and b.
    """
    while b > 0:
        a,b = b, a % b
    return a

print(gcd(50,20))
print(gcd(22,143))