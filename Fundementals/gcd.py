a = 50
b = 20

while b > 0:
    a,b = b, a % b

print("Lowest common divider: ", repr(a))