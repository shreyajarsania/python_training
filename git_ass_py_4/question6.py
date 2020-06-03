############################################################################
 #
 # Write a Python program to find the second smallest number in a list.
 #
############################################################################

#take input from user
items = input("Enter the list separated by , ")
items = items.split(",")

# take the amswer in minmum
minimum = int(items[0])

# take int inputs in converted list
converted = []

for each in items:
    if(each.isdigit() == False): # validate the input
        print("Enter a valid number")
        exit(0)

    each = int(each, 10)# convert string to int
    converted.append(each)
    if(each < minimum):
        minimum = each


# remove minimum value
for each in converted:
    if(each == minimum):
        converted.remove(each)

minimum = converted[0]
for each in converted:
    if(each < minimum):
        minimum = each

print("2nd minimum from all the elements is {}". format(minimum))
