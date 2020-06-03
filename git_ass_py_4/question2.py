############################################################################
 #
 # Write a program that accepts a comma separated sequence of words as input
 # and prints the words in a comma-separated sequence after sorting them 
 # alphabetically.
 #  Suppose the following input is supplied to the program:
 #	without,hello,bag,world
 #  Then, the output should be:
 #	bag,hello,without,world
 #
############################################################################

#taking input from user
words = input("Enter words ")
words = words.split(",")

# sorting and storing words
words.sort()

length = len(words) - 1
for each in words:
    if  length == 0:
        print(each)
    else:
        print(each, end = ",")
    length -= 1
