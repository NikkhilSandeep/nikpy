def my_generator(n):
    value = 0
    while value < n:
        yield value
        value += 1
for value in my_generator(3):
    print(value)

def factorial(n):
  print(f"factorial() called with n = {n}")
  return_value = 1 if n <= 1 else n * factorial(n -1)
  print (f"-> factorial({n}) returns {return_value}")
  return return_value
factorial(4)

def gcd(a, b):
   if a == b:
      return a
   elif a < b:
      return gcd(b, a)
   else:
      return gcd(b, a - b)
a = 20
b = 4
print(gcd(a, b))
