###########################
#      Dictionaries [ii]
#      Name: Nuria
#      Date: 26/05/22
############################

person ={'name':'Nuria',  'gender':'female','phone_number':'3456',  'location':'nairobi'}
#print(person)

# the get method takes in two arguments : (key) and (product)
#print(person.get["'password' , the  'location' key is non existent"])


Mary = ['beef' , 'chicken' , 'vegetable']
Jane = ['rice' , 'ugali' , 'potato']

fav_foods ={
    'Mary':['beef','chicken', 'vegetable'], 
    'Jane':['rice','ugali','potato'],
    }
#print(Mary)
#print(Jane)

for key, value in fav_foods.items():
    print(f"{key}:{value}")