#######################################################################################
 #
 # Write programs using below scenarios:
 #	1) Function with parameters
 #	2) Function with return value
 #	3) Function with parameter like (List, Set and Dicitionary)
 #	4) Default arguments in function
 #
######################################################################################
 
#1) Function with parameters

print("Functions with parameters")
def fun(age, std):
    print("Age: ", age)
    print("std: ", std)

fun(10, 45)
fun(std = 3, age = 19)
print()


#2) Functions with retrun value

print("Functions with retrun value")
def my_fun(num1, num2):
    sum = num1 + num2
    return sum

print("Sum of 10 and 20 is", my_fun(10, 20))
print()

#3) Function with parameters like(list, dictionary, and set)

def list_dict_set(list , dict, set ):
    
    print('add 4 to values of list')
    i = 0
    for all in list:
        list[i] += 4
        i += 1

    print('append in dictionary')
    dict.update({4:16, 5:25})

    print('update given set with function set')

    set_fun = {4, 5, 6}
    set.update(set_fun)

my_list = [1, 2, 3, 4]
dictionary = {1 : 1, 2 : 4, 3 : 9}
my_set = {1, 2, 3}
list_dict_set(my_list, dictionary, my_set)

print(my_list)
print(dictionary)
print(my_set)
print()

#4) Default argumets in function

print('Default arguments in function')
def student(firstname = 'not known', lastname = 'not known', standard = 'not known'):
    print('student with name', firstname, 'and lastname', lastname, 'is studing in ', standard )

student('alice')
student(standard = '9th')
student ('john', 'mathewe', '12th')
