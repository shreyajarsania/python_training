##########################################################################
 #
 # Write a program which can filter even numbers in a list by using filter
 # function. The list is: [1,2,3,4,5,6,7,8,9,10]. 
 #
##########################################################################

#take input from user
number = input("Enter the , separated numbers ")
number = number.split(",")

number = [int(num) for num in number]

# using filter with lamda function
result = list(filter((lambda num : num % 2 == 0), number))

print("Answer using filter lambda function ",result)


# defining function
def even(num):
    if num % 2 == 0:
        return num

result = list(filter (even, number))
print("Answer using filter with function ", result)
