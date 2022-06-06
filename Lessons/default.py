def print_name(name = "kibe"):
    print(name)

print_name("kibe")

def get_sum(num1 , num2):
    sum_nums = num1 + num2
    return sum_nums

print(get_sum(7,12))

#square of numbers

def get_powers(number , power):
    power_num = number ** power
    return power_num
print(get_powers(2,4))

##full name
def get_fullname(f_name, s_name):
    full_name = f_name + s_name
    return full_name
print(get_fullname("Nuria","Salim"))

##returning a dictionary

def get_fullname(f_name, s_name):
    person ={'first':f_name ,'second': s_name}
    return person
student = get_fullname('Nuria' , 'Salim')
print(student)
#will bring error

#passing a list in a function
def greet_friends(names):
    for name in names:
        msg = "Hello " + name.title() + "!"
    print(msg)
friends =['Mary' , 'Amina' , 'Farid' , 'Ann']
greet_friends (friends)
