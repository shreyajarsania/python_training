############################################################################
 #
 # Write a Python program to find common items from two lists.
 #
############################################################################

#taking input from user
list1 = input("Enter 1st list ")
list1 = list1.split(",")
list2 = input("Enter 2nd list ")
list2 = list2.split(",")

print("Using sets")
#convert lists to set
set_list1 = set(list1)
set_list2 = set(list2)

#by intersection find common elements
result = set_list1.intersection(set_list2)

result = list(result)

print(result)

print("using for loop")

#store answer in result
result = []
for each in list1:
    if each in list2: # check if common elemets or not
        result.append(each)

print(result)
