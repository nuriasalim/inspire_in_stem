#1/usr/bin/python

###########################
#      Dictionaries
#      Name: Nuria
#      Date: 23/05/22
############################

#key value pair is values that are associated with each other
#Initializing dictionaries
#dicionaries use {}
#student{} ->empty dictionary
#add pairs
student= {"Name":"Nuria" , "Age": "20" , "Gender": "Female"}

print(student['Name'])
student["id no"] ="32940966"
student["hobby"] = "photography"
student["club"] = "Liverpool"

print(student)

#student ["favorite food"] = "Chapati"
#student ["best sport"] ="Tennis" 
#student ["home city"] = "Nairobi"

print(student)

#modifying values

student ["Age"] = "23"
print(student)

#removing value from list -> use del
del student['hobby']
print(student)


