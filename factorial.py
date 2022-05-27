
from math import factorial
#assignment on factrial
#there isnt a factorial for negative numbers
#the factorial of 0 is 1

#Find the factorial of 6 and 9

#fact = number  * ( number - 1)
number = 6
fact = (number * (number-1) * (number-2) * (number-3)* (number-4) * (number-5))
print(fact)


number = 9
fact = (number * (number-1) *(number-2) * (number-3) * (number-4) *(number-5) *(number-6) *(number-7) *(number-8))
print(fact)

#another way of doing this is:

number = int(input("Enter the number "))
factorial = 1

if number < 0:
  print("factorial of negative doesnt exist")

elif number == 0:
  print("factorial of 0 == 1")

else:
   for i in range (1 , number + 1):
        factorial = factorial * i
print("factorial of number is: , factorial")
print(factorial)

 
