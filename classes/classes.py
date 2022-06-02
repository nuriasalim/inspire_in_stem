#1/usr/bin/python

###########################
#      Classes
#      Name: Nuria
#      Date: 02/06/22
############################

#A class is a user-defined blueprint or prototype from which objects are created.
#Classes provide a means of bundling data and functionality together. 
#Creating a new class creates a new type of object, allowing new instances of that type to be made. 
#Each class instance can have attributes attached to it for maintaining its state. 
#Class instances can also have methods (defined by their class) for modifying their state.


#class Dog: 
    #def att(name , age)
    #def breed(type, gender)

class Person:
    def __init__(self, _name, _age):
        self.name= _name
        self.age=_age

    def sayHi(self):
        print(f'Hello my name is {self.name} , and I am {self.age} years old')
        #you can use format method as above or normal method as below
        #print('Hello my name is ' + self.name , ', and I am ' + self.age ,'years old') 
person1 = Person('Bob' , str(16))
person1.sayHi()
person2 = Person('James', str(22))
person2.sayHi()

  