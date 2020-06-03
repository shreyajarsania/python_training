###############################################################################################
 #
 # Write a program that will ask number from user and check if number is even or odd.
 #
##############################################################################################

# take input form user
i = input("ENter a number to be checked ")

# input taken from user is is string from, convert it into integer
i = int(i, 10)

# logic for odd and even
if i % 2 == 0:
    print("EVEN NUMBER")
else:
    print("ODD NUMBER")
