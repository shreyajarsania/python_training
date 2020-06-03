############################################################################
 #
 # Write a Python program to get the largest number from a list. (Do not use 
 # inbuilt function "max()")
 #
############################################################################

#take input from user
items = input("Enter the list separated by , ")
items = items.split(",")

result = []

for each in items:
    if(each.isdigit() == False): # validate the input
        print("Enter a valid number")
        exit(0)

    if each not in result: # check if the number is present or not
        result.append(each)

length = len(result) - 1
for each in result:
    if  length == 0:
        print(each)
    else:
        print(each, end = ",")
    length -= 1
