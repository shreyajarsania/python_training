###########################################################################
 #
 # Write a program which can provide sum of all the elements in [1,2,3,4,5,
 # 6,7,8,9,10] (using reduce() function).
 #
###########################################################################

from functools import reduce

#take input from user
number = input("Enter the , separated numbers ")
number = number.split(",")

number = [int(num) for num in number]

# using filter with lamda function
result = reduce((lambda x,y : x + y), number)

print("sum of all the elements are ",result)
