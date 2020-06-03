########################################################################################
 #
 # Write a Python program to calculate the length of a string.
 #
#######################################################################################

# take input form user
string = input("Enter the string to find length ")

# length using len
print("Using len() function ", end = "")
print(len(string))

# for loop untill string is empty
length = 0
for i in string:
    length += 1

print("Using for loop ", end = "")
print(length)
