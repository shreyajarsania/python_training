#########################################################################
 #
 # Create one list and use below operations:
 #	1) Index slicing
 # 	2) append()
 #	3) clear()
 #	4) copy()
 #	5) count()
 # 	6) index()
 #	7) insert()
 #	8) pop()
 #	9) remove()
 #	10) sort()
 #	11) reverse()
 #	12) join()
 #	13) Nested list
 #
#########################################################################

import copy
my_list = [ 'a', 'b', 'c', 1, 2, 3, 'abc', 'lmn', 'xyz' ]

#1) slicing the list slice(start, stop, step)
print("slicing the list slice(start, stop, step)")
print(my_list[slice(5)])
print(my_list[slice(3,6)])
print(my_list[slice(3,9,2)])
print()


#2) append the list str.append(item)

print("append the list str.append(item)")
my_list.append(1.1)
my_list.append(2.2)
my_list.append(3.3)
print(my_list)
print()

#3) clear list str.clear()

print("clear list str.clear()")
my_list.clear()
print(my_list)
print()
#4) copy other list to my_list

#shallow copy

print("shallow copy")
other_list = ['x', 'y', 'z']
cpy_list1 = other_list.copy()
cpy_list2 = copy.copy(other_list)
cpy_list3 = other_list[:]

cpy_list1.append('w')
cpy_list2.append('w')
cpy_list3.append('w')

print(cpy_list1)
print(cpy_list2)
print(cpy_list3)
print(other_list)
print()

#deep copy

print("deep copy")
dcpy_list = other_list
dcpy_list.append('w')

print(dcpy_list)
print(other_list)
print()

#5) count no. of repetation using count()

print("count no. of repetation using count()")
check_list = ['a', 'b', 'c', 'a', 'b', 'c' ]
string = 'it is a good day and a day to good '

print(check_list.count('a'))
print(string.count("good"))
print()


#6) find index of an item from the list and string

print("find index of an item from the list and string")
index_list = [ 'a', 'b', 'c', 1, 2, 3, 'abc', 'lmn', 'xyz' ]

print(index_list.index('abc'))
print(string.index('good'))
print()


#7) insert item in between the list

print("insert item in between the list")
insert_list = [1, 2, 3, 'a', 'b', 'c']
insert_list.insert(3, "inserted")

print(insert_list)
print()

#8) pop the index to be removed to be removed

print("pop the index to be removed to be removed")
pop_list = [1, 2, 3, 'a', 'b', 'c']
pop_list.pop(4)

print(pop_list)
print()

#9) remove item from the list

print("remove item from the list")
remove_list = [ 1, 2, 3, 'a', 'b', 'c']
remove_list.remove(3)

print(remove_list)
print()

#10) sorting the list

print("sorting the list")
sort_list = [ 5, 3, 2, 1, 8, 4, 9, 6, 10, 7]
sort_list.sort()

print(sort_list)
print()

#11) reverse the list items

print("reverse the list items")
reverse_list = [ 1, 2, 3, 'a', 'b', 'c']
reverse_list.reverse()

print(reverse_list)
print()

#12) join list and string with a separator

print("join list and string with a separator")
join_list = ["abc", "xyz", "lmn"]
joint_list = "%".join(join_list)

print(joint_list)
print()

#13) nested list

print("nested list")
nested_list = [ [5, 3, 2], [1, 8, 4], [9, 6, 10, 7]]

print(sorted(nested_list))

append_list = [result for num in nested_list for result in num]
print(append_list)
