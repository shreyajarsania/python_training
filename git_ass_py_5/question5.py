############################################################################
 #
 # Write a program which can map() to make a list whose elements are square
 # of elements in [1,2,3,4,5,6,7,8,9,10].
 #
############################################################################

#take input from user
number = input("Enter the , separated numbers ")
number = number.split(",")

number = [int(num) for num in number]

# using map with lamda function
result = list(map(lambda x : (x * x), number))
print("Answer using map lambda function ",result)


# defining function
def square(num):
    return num * num

result = list(map (square, number))
print("Answer using map with function ", result)

