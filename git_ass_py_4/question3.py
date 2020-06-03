############################################################################
 #
 # Write a program that accepts a sequence of whitespace separated words as 
 # input and prints the words after removing all duplicate words and sorting
 # them alphanumerically.
 #  Suppose the following input is supplied to the program:
 #	hello world and practice makes perfect and hello world again
 #  Then, the output should be:
 #	again and hello makes perfect practice world
 #
############################################################################

#taking input from user
words = input("Enter words ")
words = words.split(" ")

# sorting and storing words
words.sort()

# store result in empty list
result = []
for each in words:
    if each not in result: # check if that word already exists in result or not
        result.append(each)

for each in result:
        print(each, end = " ")
print()
