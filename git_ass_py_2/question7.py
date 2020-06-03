############################################################################################
 #
 # Write a Python program that will ask number to user and check if the number is divisible 
 #  by 7 and multiple of 5?
 #
############################################################################################

# take input from user
i = input("Enter the number to be checked ")

# convert string to integer
i = int(i, 10)


# check for divisibility
if (i % 7 == 0) & (i % 5 == 0):
    print("DIVISIBLE BY 7 AND 5 BOTH")

elif i % 7 == 0:
    print("DIVISIBLE BY ONLY 7")

elif i % 5 == 0:
    print("DIVISIBLE BY ONLY 5")

else:
    print("NOT DIVISIBLE BY 7 OR 5")
