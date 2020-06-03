############################################################################
 #
 # Write a python program which takes comma separated numbers from user and 
 # print sum of all the numbers.
 #
############################################################################

from functools import reduce

numbers = input("Enter the , separated numbers ")
numbers = numbers.split(",")

numbers = [int(num) for num in numbers]

result = reduce((lambda sum, num : sum + num), numbers)

print("Sum of all the numbers using reduce function with lambda is: ", result)
print()


#define a function to sum all values in list
def sum_num(list):
    sum = 0
    for num in list:
        sum += num
    return sum

print("Sum of all numbers using sum function is : ", sum_num(numbers))
