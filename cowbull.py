import random 
def Digits(num):
    return [int(i) for i in str(num)]     
def theDuplicates(num):
    number = Digits(num)
    if len(number) == len(set(number)):
        return True
    else:
        return False   
def TakeNum():
    while True:
        num = random.randint(1000,9999)
        if theDuplicates(num):
            return num
def noOfBullsCows(num,guess):
    bull_cow = [0,0]
    number = Digits(num)
    guess_no = Digits(guess)
      
    for i,j in zip(number,guess_no):
          
        
        if j in number:
          
            if j == i:
                bull_cow[0] += 1
              
            else:
                bull_cow[1] += 1
                  
    return bull_cow
      
      

num = TakeNum()
noOFtries =int(input('Enter the number of tries: '))
while noOFtries > 0:
    guess = int(input("Enter the guess: "))
      
    if not theDuplicates(guess):
        print("The numbers should not be repeated")
        continue
    if guess < 1000 or guess > 9999:
        print("Enter only 4 digit number . Try again.")
        continue
      
    bull_cow = noOfBullsCows(num,guess)
    print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    noOFtries -=1
      
    if bull_cow[0] == 4:
        print("CORRECT,the number is guessed")
        break
else:
    print(f"Sorry,You are out of Tries. Number was {num}")