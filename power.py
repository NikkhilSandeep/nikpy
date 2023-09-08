base = int(input("Enter a Number"))
exponent = int(input("Enter a number"))

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))

x=39 << 3 # Bitwise left shift
y=5 >> 1  # Bitwise right shift
print(x,y)

a = 10
b = 4
 
# Print bitwise AND operation
print("a & b =", a & b)
 # Print bitwise OR operation
print("a | b =", a | b)