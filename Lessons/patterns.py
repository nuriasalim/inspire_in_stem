#get the rows 

rows = int(input("Enter number of rows"))

for i in range (rows):
    for j in range (i + 1):
        print(j + 1 , end = " ") #will print(j + 1) as 1 , 1 2, 1 2 3:
    print("\n ")

for i in range (rows):
    for j in range (i + 1):
        print(i + 1 , end = " ") #print(i + 1) this will print 1 , 2 2 , 3 3 3 
    print("\n ")


#printing a pyramid
rows = int(input("Enter number of rows"))
k = 0

for i in range (1 , rows + 1 ):
    for space in range ( 1, (rows - i) + 1):
        print( end = " " )
    while k!= (2*i - 1):
        print("n ", end =" ")
        k += 1
    k = 0
    print() 
