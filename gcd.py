gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
a = 60
b = 48
# Prints 12
print("The gcd of 60 and 48 is:", gcd(a, b))
