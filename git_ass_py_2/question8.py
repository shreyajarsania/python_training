##################################################################################################
 #
 # Write a Python program to convert temperatures to and from celsius, fahrenheit.
 # [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
 # Expected Output :
 # Enter temperatue in (°C):
 #  60
 # 60°C is 140 in Fahrenheit
 #
##################################################################################################

#take input form user
celsius = input("Enter the temperature in celsius ")

#convert string to float
celsius = float(celsius)

# calculate fahrenheit
fahrenheit = celsius * 9/5 + 32

print('{} C is {} in fahrenheit'. format(celsius, fahrenheit))
