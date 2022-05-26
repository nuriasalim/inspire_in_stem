#1/usr/bin/python

###########################
#      #multi line strings and concatination
#      Name: Nuria
#      Date: 18/05/22
############################

#slicing method
city = "Nairobi"
#print(city[:5]) -> slices the word from the front
#print(city[2:]) -> slices the word from back
print(city[:5])
print(city[2:])
print(city[-1:])

f_name= "nuria "
#change to upper case -> .upper() , to lowercase -> .lower()
print(f_name.upper())
print(f_name.lower())


#float -> int  int(x)
#int -> string str(x)

#concatination -> converting from one data types to another using str(), int(), and float()

number= 6
print(str(6))
print(int(6))
print(float(8))

x = 4
print(float(x))

y = 3.24
print(int(y))


f_name = "James"
s_name = "Corden"

full_name = f_name + s_name
print(full_name)


#the replace () method replaces existing character in a string with another 

name = "Brett Cooper"
print(name.replace('t' , 'G'))

#The split() method splits the sentences into single words hence a list
msg = "Hello there I am Nuria from Nairobi"

print(msg.split())


#The len method is used in getting the length of a string
print(len(msg))


msg = ''' I am Nuria Mohamed
 I come from Nairobi
I am learning how to code
           '''

print(msg)


