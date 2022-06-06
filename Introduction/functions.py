#1/usr/bin/python

###########################
#      Functions
#      Name: Nuria
#      Date: 31/05/22
############################

#block of code whic get executed together
#intialize the function
#calling the function

#defining a function/ initializing

from tkinter import Y


def say_hello():
    print("Hello from JKUAT")
    x =4
    y =7
    z =x + y 
    print(z)
say_hello()

def bark():
    print('Dogs bark woof!')
def meow():
    print('Cats meow')
def roar():
    print('Lions roar!')
bark()
meow()
roar()

#..........function parameters.........#
#function add two numbers

def add_numbers(x,y):
    sum_num = x + y 
    print("The sum of numbers:" , sum_num)
add_numbers (50, 40)

#function multiply two numbers

def multiply_numbers (x,y):
    multiply_numbers = x * y
    print("The product of numbers is:" , multiply_numbers)
multiply_numbers(5,6)

#function divide two numbers
def quotient_num (x ,y):
    quotient_num = x / y 
    print("The quotient of numbers is:" , quotient_num)
quotient_num(500,2)