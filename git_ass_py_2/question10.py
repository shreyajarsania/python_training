###############################################################################################
 #
 # Write a program in Python to calculate and print the Electricity bill of a given customer.
 # The customer id., name and unit consumed by the user should be taken from the keyboard and 
 # display the total amount to pay to the customer. The charge are as follow :
 #	Unit 					Charge/unit
 #	upto 199 				@1.20
 #	200 and above but less than 400 	@1.50
 #	400 and above but less than 600 	@1.80
 #	600 and above 				@2.00
 # If bill exceeds Rs. 400 then a surcharge of 15% will be charged and the minimum bill should
 # be of Rs. 100/-
 #
##############################################################################################

#take input from user
cus_id = input ("Enter customer id ")
cus_name = input ("Enter customer name ")
cus_unit = input ("Enter total units consumed by the customer")

#convert units string to int
cus_unit = int(cus_unit, 10)


# check units range and calculte money accordingly
if cus_unit <= 199:
    money = cus_unit * 1.2

elif 200 <= cus_unit < 400:
    money = 199 * 1.2 + (cus_unit - 199) * 1.5

elif 400 <= cus_unit < 600:
    money = 199 * 1.2 + 200 * 1.5 + (cus_unit - 399) * 1.8

elif cus_unit >= 600:
    money = 199 * 1.2 + 200 * 1.5 + 200 * 1.8 + (cus_unit - 599) * 2


# overwrite money if amount is less then 100, and add 15% more charges if greater than 400
if money < 100:
    money = 100 # minimum amount must be 100

elif money > 400:
    money += 0.15 * money # 15% = 0.15 surplus charges if amount is more than 400

print("Customer details : \nid: \t\t{} \nname: \t\t{} \nbill amount: \t{}". format(cus_id, cus_name, money))
