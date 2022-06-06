####Password Generator
import random


print("Welcome to our Password generator")
character ="Nuria1234!"
no_of_passwords = int(input('How many passwords would you like to generate? '))
pass_length = int(input("How many characters would you like? "))
print("Here are your passwords! ")

for password in range(no_of_passwords):
    password = ''
    for c in range (pass_length):
        password += random.choice(character)
print(password)

#assignment 
#Convert the above to class

class Password:
    def __init__ (self, _password, _character, _passlength):
        self.password = _password
        self.character = _character
        self.passlength = _passlength 
        for c in range (pass_length):
            password += random.choice(character)
    
        


         

