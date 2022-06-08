#program to check if a number or a word is a palindrome

my_str = input("Enter the character youd like to check")
my_str = str(my_str)

rev_str = reversed(my_str)

#create if statement to check if string is equal to reverse
if (my_str) == (rev_str):
    print("This is a palindrome")

else:
    print("Not a palindrome") 

    #check on coce, prog has error
