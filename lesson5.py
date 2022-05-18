#string methods
#methods are in built functions used to work on all the different data types
#\n is used to add new lines
#\t is used to add tab function

from types import MethodDescriptorType


name = "Nuria Salim"
age = 20
user_name = "Ada Lovelace"

print("My name is {} and I am {} years old".format(name , age))

#the format method
#(f "declared variables")
print(f"My name is {name} and I am {age} years old")

#the strip method
#strips out white spaces
#rstrip ->strips on the right side
#lstrip -> strips on the left side
#strip -> strips white spaces on both sides


print(user_name.strip())

#The replace() method replaces a character  in a string with another character

name = "Ada Lovelace"
print(name.replace('A' , 'I'))
print(name.replace('Ada' ,'Nuria'))



