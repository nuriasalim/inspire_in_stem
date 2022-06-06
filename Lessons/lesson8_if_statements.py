#1/usr/bin/python

###########################
#      #lists
#      Name: Nuria
#      Date: 24/05/22
############################
 
 #print(square)
squares = []
for numbers in range ( 0, 10):
    square = numbers**2
    squares.append(square)
    print(squares)
   

#print cubes
cubes= []
for numbers in range (0,10):
    cube = numbers **3
    cubes.append(cube)
    print(cubes)

#print sum of numbers
sums = []
for numbers in range (0,10):
    sum = numbers + 1
    print(sums)


#if statements
age= 24
if age >= 18:
    print('You are allowed to drive ')  
else:
    print('You are too young to drive ')


name = "Nuria"
age = input("what is your age")
account_balance = 0
if(int(age) >=25) and (int(age) <= 30):
   print("You are allowed to drive")
else:
    print("You are NOT allowed to drive")

vehicles = ['bmw', 'audi' , 'toyota' , 'mercedes' , 'jeep']


#using If statement find jeep in the list and convert to uppercase
#using for loops to print vehicles

for vehicle in vehicles:
   
   print(vehicle.title())
if (vehicle == 'jeep'):
       print(vehicle.upper())
    


