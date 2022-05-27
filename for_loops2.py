#1/usr/bin/python

###########################
#      #loops
#      Name: Nuria
#      Date: 20/05/22
############################
#about loops

school=['Joy' , 'Hope' , 'Mercy' ,'Happy']
pupil= ['Peace' , 'Patience' , 'Amani' , 'Character']

#print(pupil[0], school[0])
#print(pupil[1], school[1])
#print(pupil[2], school[2])
#print(pupil[3], school[3])

#print(f" I am {pupil[0]} and I school at {school[0]}")
#print(f" I am {pupil[1]} and I school at {school[1]}")
#print(f" I am {pupil[2]} and I school at {school[2]}")
#print(f" I am {pupil[3]} and I school at {school[3]}")

#how to make the above lines into one code line by using loops

for pupil in pupil: 
    print(f'Hello I am {pupil}')

for school in school:
    print(f'My school is {school}')

# Example 3


vehicles = ['bmw', 'audi' , 'toyota' , 'mercedes' , 'jeep']
#using If statement find jeep in the list and convert to uppercase
#using for loops to print vehicles

for vehicle in vehicles:
   
   print(vehicle.title())
if (vehicle == 'jeep'):
       print(vehicle.upper())
    