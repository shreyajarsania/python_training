############################################################################
 #
 # Create one dictionary and use below operations:
 #	1) clear()
 #	2) copy()
 #	3) get()
 #	4) items()
 #	5) keys()
 #	6) pop()
 #	7) popitem()
 #	8) update()
 #	9) Nested dictionary
 #	10) Dictionary in list
 #	11) List in dictionary
 #
############################################################################

#1) clear in dictionary

print("clear in dictionary")
dictionary = {'roll_no.' : 1, 'name' : "Shreya", 'standard' : '9th'}

print(dictionary)
dictionary.clear()

print(dictionary)
print()


#2)copy dictionary

print("copy one dictionary to another")
old_dictionary = {'roll_no.' : 1, 'name' : "Shreya", 'standard' : '9th'}
new_dictionary = old_dictionary.copy()
print(new_dictionary)
print()


#3) get() in dictionary

print("get in dictionary")
dictionary = {'roll_no.' : 1, 'name' : "Shreya", 'standard' : '9th'}
x = dictionary["roll_no."]

print("using direct method", end = " ")
print(x)

x =  dictionary.get('name')
print("using get method", end = " ")
print(x)
print()


#4) items in dictionary

print("items in dictionary")
print("student: %s" % dictionary.items())
print()

#5)keys of dictionary

print("keys in dictionary")
print("student info = %s" % dictionary.keys())
print()

#6)pop in dictionary

print("pop roll_no. in dictionary")
dictionary.pop("roll_no.")
print(dictionary)
print()

#7) popitems in dictionary

print("pop last added item in dictionary")
dictionary = {'roll_no.' : 1, 'name' : "Shreya", 'standard' : '9th'}
dictionary.popitem()

print(dictionary)
print()

#8) update in dictionary

print("update in dictionary")
dictionary = {'roll_no.' : 1, 'name' : "Shreya", 'standard' : '9th'}
dictionary.update({'standard' : '10th'})

print(dictionary)
dictionary.update({'school' : 'xyz'})

print(dictionary)
print()

#9) Nested dictionary

print("Nested dictionary")
dictionary = {1 : {'roll_no.' : 3, 'name' : "Ssdfgh", 'standard' : '9th'},
              2 : {'roll_no.' : 5, 'name' : "Shrfds", 'standard' : '7th'},
              3 : {'roll_no.' : 2, 'name' : "Shrrhj", 'standard' : '4th'}}

for subdict in dictionary:
    print(dictionary[subdict]['name'])

print()


#10)List in dictionary

print("List in dictionary")
dictionary = {'num' : [1, 2, 3], 'alpha' : ['a' ,'b', 'c'], 'string' : ['abc', 'lmn', 'xyz']}

dictionary['num'].pop(0)
dictionary['alpha'].pop(1)
dictionary['string'].pop(2)

print(dictionary)
print()
