#lists -> should have box brackets

motocycle_owner= ("Mojo Jojo")
motorcycle = ['honda' , 'yamaha' , 'suzuki']
plate_number = ['H1234' , 'Y1234' , 'S1234']
#print(motorcycle)

#accessing list items using the index
#print(motorcycle[2])

#print(motorcyvle[3]) -> cannot shot this since its not within the range

#motorcycle[0]= "Bugatti"-> replacing items in the list -> index 0 is the first elemt-. honda

#print(motorcycle)
#the above replaces index 1 with bugatti
#motorcycle[0]= "Bugatti"
#print(motorcycle)

#print("i love"+  str(motorcycle[1]))

#adding element in a list
#motorcycle.append('Bugatti') 
#using .append-> adds the item you wwant to the list
#print(motorcycle)

#print each morocycle and their plate number

#print(motorcycle[1],plate_number[1])
#print(motorcycle [0],plate_number[0], motorcycle[1],plate_number[1])
#print("i love"  +  str(motorcycle[0]), plate_number[0])

#LEARNING TO DELETE AN ITEM FROM A LIST -- del, TO ADD -- append
#del motorcycle[0]
#print(motorcycle)
#popped ->pop()
#popped_motorcycle = motorcycle.pop()


#task-> print a statement
#my name is Mojo Jojo and I own motorcycle plate number
#example 1
#print(f" My name is {motocycle_owner} and I own {motorcycle[1]} {plate_number[1]}")
#example 2
#print(f" My name is {motocycle_owner} and I own both {motorcycle[1]} {plate_number[1]} and {motorcycle[2]} {plate_number[2]} ")
#example 3
#print(f" My name is {motocycle_owner} and I own {motorcycle[1]} plate number {plate_number[1]}")

#removing a item from a list

motorcycle.remove('suzuki')
print(motorcycle)


