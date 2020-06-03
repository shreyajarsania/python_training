############################################################################
 #
 # Create object of below datatype using comprehension:
 #      1. list
 #      2. Tuple
 #      3. Dictionary
 #      4. Set
 # 
############################################################################

#1) object for list

print("for list")
my_list = [i + 4 for i in range(5)]
print(my_list)


#2) object of tuple

print("for tuple")
my_tuple = tuple(i + 4 for i in range(5))
print(my_tuple)


#3) object of dictionary

print('for dictionary')
dictionary = {key : value for key, value in {'roll_no': 2, 'name' : 'abc'}.items()}
print(dictionary)


#4) object for set

print('for set')
my_set = { i + 4 for i in range(5)}
print(my_set)
