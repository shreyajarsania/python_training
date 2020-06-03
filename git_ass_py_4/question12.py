##################################################################################
 #
 # Write a Python program to combine two dictionary adding values for common keys. 
 #	d1 = {'a': 100, 'b': 200, 'c':300}
 #	d2 = {'a': 300, 'b': 200, 'd':400}
 #	Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
 #
##################################################################################

dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}

dict3 = {}
for key in dict1: # access key of 1st dictionary
    if key in dict2: # check if exists, add them up
        dict1[key] = dict1[key] + dict2[key]

dict2.update(dict1)
print(dict2)
