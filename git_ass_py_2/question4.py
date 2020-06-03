###############################################################################################
 #
 # Write a Python program to find the first appearance of the substring 'not' and 'poor' from 
 # a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with
 # 'good'. Return the resulting string.
 #	Sample String : 'The lyrics is not that poor!'
 # 			'The lyrics is poor!'
 #	Expected Result : 'The lyrics is good!'
 #			  'The lyrics is poor!'
 #
##############################################################################################

# get input from user
string = input("Enter the string ")

# get the indexs of not and poor
value1 = string.find('not')
value2 = string.find('poor')

#if not occured before poor replace the string with good
if value1 < value2:

    string = string.replace(string[value1 : value2 + 4], 'good')

print(string)
