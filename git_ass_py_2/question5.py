###############################################################################################
 #
 # Write a Python program to remove the nth index character from a nonempty string.
 #	Sample:
 #		Enter string: "Hello Team"	
 #		Enter index to remove: 3
 # 	Expected Output:
 #		"Helo Team"
 #
##############################################################################################

# take input form user
string = input("Enter the string ")

# check if string is empty
if len(string) == 0:
    print("string cannot be empty")
else:
    c = input ("Enter the index to be removed")
    c = int(c, 10) # when input taken from user, it is in string format, convert it into integer

    string = string[0 : c] + string[c + 1 :]
    print(string)

