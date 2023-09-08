def isPalindrome(s):
    return s == s[::-1]
s = "malayalam"
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")

def fact(n):  
    return 1 if (n==1 or n==0) else n * fact(n - 1);  
num = 5  
print("Factorial of",num,"is",)  
print(fact(num))

def fib(n):
 a = 0
 b = 1
 if n == 1:
  print(a)
 else:
  print(a)
  print(b)
  for i in range(2,n):
   c = a + b
   a = b
   b = c
   print(c)
fib(10)

for i in range(5):
    print(i, end=" ")
print()

numbers = [1,2,3,4,5,1,4,5]
Sum = sum(numbers)
print(Sum)
Sum = sum(numbers, 10)
print(Sum)