#write a program to withdraw 25000 if the account balance is btwn 100000 to 200000

acc_bal = input("Enter the account balance")
if (int(acc_bal)>100000) and (int(acc_bal)<200000):
    acc_bal = acc_bal - 25000
    print("We have deducted ksh 25000")
    print("Your account balance is 25000")


#30% if acc balance is btwn 500k and 1M   

if(int(acc_bal)>500000) and (int(acc_bal)<1000000):
    acc_bal = acc_bal - (0.3*acc_bal)
    float(acc_bal)- (0.3* acc_bal)
    print("No deductions done")



#30% if acc balance is btwn 500k and 1M



#above 1M deduct 700k

