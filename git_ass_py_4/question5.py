############################################################################
 #
 # Write a Python program to get the largest number from a list. (Do not use 
 # inbuilt function "max()")
 #
############################################################################

#take input from user
items = input("Enter the list separated by , ")
items = items.split(",")

# take the amswer in maximum
maximum = int(items[0])
for each in items:
    if(each.isdigit() == False): # validate the input
        print("Enter a valid number")
        exit(0)

    each = int(each, 10)# convert string to int
    if(each > maximum):
        maximum = each

print("maximum of all the elements is {}". format(maximum))
