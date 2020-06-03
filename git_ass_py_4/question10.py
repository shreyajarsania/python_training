############################################################################
 #
 # Write a Python script to generate and print a dictionary that contains a
 # number (between 1 and n) in the form (x, x*x).
 # 	Sample Dictionary ( n = 5) :
 #	Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 
 #
############################################################################

#taking input from user
num= input("Enter the number ")

# validation
if num.isdigit == False:
    print("Enter a valid number")
    exit(0)

# convert string to int
num = int(num, 10)

#add items to this empty dictionary
dictionary = {}

for key in range(num + 1):
    dictionary[key] = key * key # add items to dictionary

print(dictionary)
