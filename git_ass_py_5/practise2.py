######################################################################
#
#Write program using each function. (using lambda function and list.)
#
######################################################################

from functools import reduce
#1) filter

print("filter")
My_list = [1,2,3,4]
result = list(filter(lambda x : (x % 2 != 0), My_list))
print(result)
print()


#2) map
print("map")
result = list(map(lambda x : (x * 2), My_list))
print(result)
print()

#3) reduce
print("reduce")
result = reduce((lambda x,y : x + y), My_list)
print(result)
