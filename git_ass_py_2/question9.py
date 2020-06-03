##################################################################################################
 #
 # Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 
 # it will return 20.
 #
##################################################################################################

# take input from user

num1 = input("Enter 1st number")
num2 = input("Enter 2nd number")

# convert string to float
num1 = float(num1)
num2 = float(num2)

# sum
sum_num = num1 + num2

# check if sum is between 15 to 20
if 15 <= sum_num <= 20:
    print('20')
else:
    print(sum_num)
