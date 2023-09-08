class Check :
    def __init__(self,number) :
        self.num = number 
    def isPalindrome(self) :
        temp = self.num
        result = 0
        while(temp != 0) :
            rem = temp % 10
            result =  result * 10 + rem
            temp //= 10
        if self.num == result :
            print(self.num,"is Palindrome")
        else :
            print(self.num,"is not Palindrome") 
if __name__ == "__main__" :
    num = 151
    check_Palindrome = Check(num)
    check_Palindrome.isPalindrome()

class Nikki:
    def findFact(self, n):
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f
print("Enter a Number: ", end="")
num = int(input())
ob = Nikki()
print("\nFactorial of", num, "=", ob.findFact(num))

class Operation:
    def fibonacci(n):
      n = 10
      num1 = 0
      num2 = 1
      next_number = num2 
      count = 1
 
      while count <= n:
       print(next_number, end=" ")
       count += 1
       num1, num2 = num2, next_number
       next_number = num1 + num2
      print()
num=10
om=Operation()
print("Fibonacci:",om.fibonacci())




         