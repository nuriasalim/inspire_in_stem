#1/usr/bin/python

###########################
#      Tuples
#      Name: Nuria
#      Date: 31/05/22
############################

#list
fruits = ['mango' , 'guava' , 'orange']

fruits[2]= 'apple'
print(fruits)

#tuple

new_fruits =('mango', 'lime' , 'guava' , 'banana')
#new_fruits[1] = 'apple' #error= object doesnt support item assignment
print(new_fruits[2])

cars= ('audi', 'bmw' ,'vw' , 'toyota')
cars=('nissan', 'bmw' , ' vw' , 'toyota')
print(cars)

fav_foods = ('nyamachoma', 'mutura' , 'ugali')
for fav_food in fav_foods:
    print(fav_food)
    
