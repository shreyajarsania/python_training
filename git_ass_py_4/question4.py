############################################################################
 #
 # Write a Python program to sum all the items in a list.
 #
############################################################################

#take input from user
items = input("Enter the list separated by , ")
items = items.split(",")

# take the amswer in sum
sum_all = 0
for each in items:
    if(each.isdigit() == False): # validate the input
        print("Enter a valid number")
        exit(0)

    each = int(each, 10)# convert string to int
    sum_all += each

print("sum of all the elements is {}". format(sum_all))
