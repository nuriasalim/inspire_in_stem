#1/usr/bin/python

###########################
#      Dictionaries
#      Name: Nuria
#      Date: 23/05/22
############################

#dictionariy is a collection of key values,  associated with each other
#syntax: dictionary= {'key': 'value'}
#Initializing dictionaries
#dicionaries use {}
#student{} ->empty dictionary

#add pairs
from re import T


student= {"Name":"Nuria" , "Age": "20" , "Gender": "Female"}

#print(student['Name'])
student["id no"] ="32940966"
student["hobby"] = "photography"
student["club"] = "Liverpool"

print(student)

student ["fav food"] = "Chapati"
student ["best sport"] ="Tennis" 
student ["home city"] = "Nairobi"

#print(student)

#modifying values

student ["Age"] = "23"
#print(student)

#removing value from list -> use del
del student['hobby']
#print(student)

#example 2 of dictionaries 25/05/2022

colors = {'Color':'Red'}
list_names = {'name':'Nuria'}
vehicle= {'Type':'Toyota', 'plate_number':'KY456'}
print(colors)
#printing using the type[] method
print(list_names ['name'])
print(vehicle ['Type'])

#accessing only values in a dictionary by using the key
#You can access the value of an element inside a dictionary using the 'key': e.g
print(vehicle['Type'])
print(vehicle['Type'], vehicle['plate_number'])

person = {'name': 'Nuria'}
location = {'address':'Nairobi'}
print(person['name'], location['address'])

person ={'name':'Nuria','gender':'female','phone_number':'3456', 'location':'nairobi'}
print(person)
print(person['name'], person['gender'], person['phone_number'])

#adding a value -> dictionary ["key"] = "value"
person ["Age"] = "23"
print(person)

person["colour"] = "BLUE"
print(person)
print(person['name'], person["Age"], person['colour'])

#deleting a value 
del person['location']
print(person)

#looping over dictionaries
person ={'name':'Nuria', 
    'gender':'female',
    'phone_number':'3456', 
    'location':'nairobi'}
print(person)

for key, value in person.items():
    print(f"{key}:{value}")


colors = ['red' , 'green', 'blue', 'purple']

i = 0
while i < len(colors):
    if(colors[0] == 'red'):
        print(colors[0].upper())
        i += 1   #this closes the loop, so that the value is not run so many times

for color in colors:
    if(colors[0] =="red"):
        print(colors[0].upper())
        i += 1 

for color in colors:
    if(colors[0] == "red",colors[1]== "green", colors[2]== "blue", colors[3]== "purple"):
        print(colors[0].upper() , colors[1].upper(),colors[2].upper(), colors[3].upper())