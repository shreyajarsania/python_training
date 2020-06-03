############################################################################
 #
 # Write a Python program to clone or copy a list.
 #
############################################################################

import copy
#take input from user
main_list = input("Enter 1st list separated by , ")
main_list = main_list.split(",")

#shallow copy
print("shallow copy")
cpy_list1 = main_list.copy()
cpy_list2 = copy.copy(main_list)
cpy_list3 = main_list[:]

cpy_list1.append('w')
cpy_list2.append('w')
cpy_list3.append('w')

print("1st copy list {}". format(cpy_list1))
print("2nd copy list {}". format(cpy_list2))
print("3rd copy list {}". format(cpy_list3))
print("main list \t{}". format(main_list))
print()

#deep copy

print("deep copy")
dcpy_list = main_list
dcpy_list.append('w')

print("Deep copied list {}". format(dcpy_list))
print("Main list \t{}". format(main_list))
print()

