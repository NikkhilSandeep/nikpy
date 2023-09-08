message = 'pyTHon is fun'
print(message.upper())
print(message.lower())

list = [2, 4, 7, 10, 23, 25]
for num in list:
    if num % 2 != 0:
       print(num, end=" ")


d={'apple': 10, 'mango': 20, 'pineapple': 25, 'orange': 30, 'strawberry': 50, 'jackfruit': 10}
d = {k:v for (k,v) in d.items() if v>20}
print(d)






