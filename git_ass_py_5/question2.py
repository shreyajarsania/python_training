###############################################################################
 #
 # Define a function that can accept two strings as input and print the string
 # with maximum length in console. If two strings have the same length, then 
 # the function should print all strings line by line.
 #
###############################################################################

# define the function
def string_len(str1, str2):

    #compare lengths
    if(len(str1) - len(str2) > 0):
        return str1
    elif(len(str1) - len(str2) < 0):
        return str2
    else:
        return 'both'

# take input from user
string1 = input("Enter 1st string ")
string2 = input("Enter 2nd string ")

# check if fuction retrun both
if(string_len(string1, string2) == 'both'):
    print(string1)
    print(string2)
else:
    print(string_len(string1, string2))

