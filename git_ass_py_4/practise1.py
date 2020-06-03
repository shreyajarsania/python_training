############################################################################
 #
 # Iterate below datatypes with loop(use while and for both loops):
 # 	1. list
 #	2. Tuple
 #	3. Dictionary
 #	4. Set
 # 
############################################################################

#1) for and while for list

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("for loop for list")
for alpha in my_list:
    print(alpha, end = " ")

print()

print("while loop for list")
i = 0
while i < len(my_list):

    print(my_list[i], end = " ")
    i += 1

print()


#2) for and while for tuple

my_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print("for loop for tuple")
for alpha in my_tuple:
    print(alpha, end = " ")

print()

print("while loop for tuple")
i = 0
while i < len(my_tuple):

    print(my_tuple[i], end = " ")
    i += 1

print()

#3) for and while for dictionary 

dictionary = {'roll_no' : 1, 'name' : 'abc', 'std' : '4th'}

print("for loop for dictionary")
for key, value in dictionary.items():
    print(key, value, end = " ")

print()

print("while loop for dictionary")
key = list(dictionary.items()) # make dictionary to list
i = 0
while i < len(key):
    print(key[i], end = " ")
    i += 1

print()


#4) for and while for Set

my_set = ['abc', 'lmn', 'xyz']

print("for loop for set")
for items in my_set:
    print(items, end = " ")

print()

print("while loop for set")
set_list = list(my_set)
i = 0
while i < len(set_list):
    print(set_list [i], end = " ")
    i += 1

print()

