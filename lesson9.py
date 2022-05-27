#1/usr/bin/python

###########################
#      Foor Loops ; even, odd, prod of even, sum of even , factorial
#      Name: Nuria
#      Date: 26/05/22
############################


for number in range (0,20):
    print(number)

for number in range (0,10):
   print(number % 2)

for number in range (0,10):
    if (number %2== 0):  #-> prints all even numbers in the range
        print(number)

##sum of all even numbers between 0 and 50

sum = 0   #->initializing 
for number in range(0,20):
    if(number % 2 == 0):  #even numbers
       sum = (sum +number)
print(sum)    #-> should be directly below the for loop  line

##product of all numbers between range 0 and 50

prod = 1  
for number in range (0,20):
    if (number %2 == 1):  #odd numbers
        prod =(prod * number)
print(prod)


#factorial of a number is the multiplication of a number and its successive numbers before it till 1
#e.g factorial of 6! = 6*5*4*3*2*1 and factorial of 9!

#fact = number  * ( number - 1)
number = 6
fact = (number * (number-1) * (number-2) * (number-3)* (number-4) * (number-5))
print(fact)

number = 0 #initialise
while number < 10:
    print(number)
    number= number +1 

num = 10
while num < 10:
      if (num % 2 == 0):
           print(num)     #-> did not run, repeat program
           
      
       
    