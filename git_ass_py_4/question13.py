##################################################################################
 #
 # Using list and dictionary write a program to create database of student which 
 # includes name, marks of chem., Phy. and Maths.
 # This database should provide modification and display based on console.
 # Supported command to add student in list, delete student from list and display
 # student data.
 #	add [student_name] [chem. marks] [Phy. marks] [Maths marks]
 #	remove [student_name]
 #	remove [student_index]
 #	display [student_name]
 #	display [student_index]
 #    Sample Output:
 #	add Abhi 0 90 80 85
 #	add Khusboo 1 99 89 88
 #	display Abhi
 #      Name: Abhi chemistry:90 Physics:80 Maths:85 
 #	display 0
 #	Name: Abhi chemistry:90 Physics:80 Maths:8
 #	remove Abhi
 #	Details of Abhi removed from the database.
 #	remove 0
 #	Details of Abhi removed from the database.
 #
##################################################################################

# take input from user
command = input("Enter exit to exit the database \n")
command = command.split(" ")

# put data in the dictionary
dictionary = {}
# store data in form of list 
index_list = []
name_list = []
ch_list = []
phy_list = []
math_list = []

while command[0] != 'exit': # loop till exit command is given

    if command[0] == 'add': # if command is add
        if len(command) < 6:
            print("Enter proper command")
        else:
            #append the data into their respective lists
            name_list.append(command[1])
            dictionary['Name'] = name_list
        
            index_list.append(command[2])
            dictionary['index'] = index_list
        
            ch_list.append(command[3])
            dictionary['Chemistry'] = ch_list
        
            phy_list.append(command[4])
            dictionary['Physics'] = phy_list
        
            math_list.append(command[5])
            dictionary['Math'] = math_list

    elif command[0] == 'display': # if command is display
        
        if len(command) < 2:
            print("Enter proper command")

        else:
            if command[1].isdigit() == True: # if display is accessed through index
                num = 0
                if command[1] not in index_list: # check if index number exists
                    print('Student not registered')
                else:
                    for index in index_list:
                        if index == command[1]: # find the index
                            break
                        num += 1
            
                    print('Name:', name_list[num], end = ' ')
                    print('Chemistry:', ch_list[num], end = ' ')
                    print('physics:', phy_list[num], end = ' ')
                    print('Math:', math_list[num], end = ' ')
                    print()
        
            else: # if display accessed through name
                num = 0
                if command[1] not in name_list: # check if name exists
                    print("Student not registered")
                else:
                    for name in name_list:
                        if name == command[1]: # find the name
                            break
                        num += 1
            
                    print('Name:', name_list[num], end = ' ')
                    print('Chemistry:', ch_list[num], end = ' ')
                    print('physics:', phy_list[num], end = ' ')
                    print('Math:', math_list[num], end = ' ')
                    print()

    elif command[0] == 'remove': # if command is remove

        if len(command) < 2:
            print("Enter proper command")

        else:
            if command[1].isdigit() == True: #if remove is accessed through index
                num = 0
                if command[1] not in index_list: # check if index number exists
                    print('Student not registered')
                    
                else:
                    for index in index_list:
                        if index == command[1]: # find index
                            break
                        num += 1
            
                    print("Details of {} removed form the data base". format(name_list[num]))
                    name_list.pop(num)
                    index_list.pop(num)
                    ch_list.pop(num)
                    phy_list.pop(num)
                    math_list.pop(num)
        
            else: #if remove accessed through name
                num = 0
                if command[1] not in name_list: # check if name exists
                    print("Student not registered")
                    exit(0)
                else:
                    for name in name_list:
                        if name == command[1]: # find name
                            break
                        num += 1
            
                    print("Details of {} removed form the data base". format(name_list[num]))
           
                    name_list.pop(num)
                    index_list.pop(num)
                    ch_list.pop(num)
                    phy_list.pop(num)
                    math_list.pop(num)
    
    else:
        print("Enter a valid command") # if command is none of the above
        print("MENU : enter all the commnands in lower case")
        print("add \t-> to add data to database")
        print("display \t-> to display data")
        print("remove \t-> to remove data from the data base")

    command = input("Enter exit to exit the database \n") # get next command
    command = command.split(" ")
