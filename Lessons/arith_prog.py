#1/usr/bin/python

###########################
#      Arithmetic Progression
#      Name: Nuria
#      Date: 27/05/22
############################

#Step 1 – Take the input of a ( the first term ), d( the step ), and n ( the number of terms )
#Step 2 – Use for loop from 1 to n+1 and compute the nth term

# 1. Take input of 'a','d' and 'n'

a = int(input("Enter the value of a "))
d = int(input("Enter the value of d "))
n = int(input("Enter the value of n "))

# 2.
for i in range (1, n + 1):
    n_term = a + (i-1) * d
    print(n_term)
 
sum_n = (n_term/2) * (2 * a + (n-1) * d)
print(sum_n)


#GEOMETRIC PROGRESSION ASSIGNMENT