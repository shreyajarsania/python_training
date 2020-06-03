##########################################################################################################
 #
 # Create one set and use below operations:
 #	1) union()      (also do same operation using "|" opertor)
 #	2) intersection (also do same operation using "&" opertor)
 #	3) difference() (also do same operation using "-" opertor)
 #	4) issubset()   (also do same operation using "<=" opertor)
 #	5) issuperset() (also do same operation using ">=" opertor)
 #
##########################################################################################################

#1)union in set

print("Union of all sets")
set1 = {'a', 'b', 'c'}
set2 = {'d', 'e', 'f'}
set3 = {'g', 'h' ,'i'}

print(set1.union(set2, set3))
print()


#2) intersection in set

print("intersection in set1")
set1 = {'a', 'b', 'c'}
set2 = {'b', 'c', 'd'}
set3 = {'b', 'c' ,'d', 'e'}

print(set1.intersection(set2, set3))
print()


#3) difference in set

print("difference in set1")
set1 = {'a', 'b', 'c'}
set2 = {'b', 'c', 'd'}
set3 = {'b', 'c' ,'d', 'e'}

print(set1.difference(set2, set3))
print()


#4) issubset in set

print("check if set2 is subset of set1")
set1 = {'a', 'b', 'c'}
set2 = {'b', 'c'}

print(set2.issubset(set1))
print()


#5) issuperset in set

print("check if set1 is superset of set2")
set1 = {'a', 'b', 'c'}
set2 = {'b', 'c'}

print(set1.issuperset(set2))
