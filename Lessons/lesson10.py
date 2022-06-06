#writing a program to checkif a number is divisible by 5 or 7
#check on pseudo codes


num= int(input("Enter the number"))
# div = int("Enter the number")
#you can use 'and' statement / 'or' statement
if(num%5==0) or (num%7==0):   
    #print(num, "is divisible by 5 and 7") #OR

    print(f"The number {num} is divisible by 5 or 7")
else: 
    #print(num, "is not divisible by 5 and 7") #OR

    print(f"The number {num} is not divisible by 5 or 7")

