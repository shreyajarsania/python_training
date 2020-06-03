###############################################################################
 #
 # Define a function which can compute the sum of two numbers.
 #
###############################################################################

# define function to sum two numbers
def sum_of(num1 = 0, num2 = 0):
    sum = num1 + num2
    return sum

#take input from user
user = input("Enter two numbers ")

#validate the numbers
if user[0].isdigit() == False or user[2].isdigit() == False:
    print("Enter a valid number")
    exit(0)

# convert strings to integers
num1 = int(user[0])
num2 = int(user[2])

print("sum of {} and {} is {}". format(num1, num2, sum_of(num1, num2)))
