#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   Hiroyuki Takechi
# Date:  May 7, 2017
#-------------------------------------------------#

#Step 1: create the text file with data
#lstRow0 = ["Task", "priority"]
#lstRow1 = ["Clean House", "low"]
#lstRow2 = ["Pay Bills", "high"]
#lstTable = [lstRow0,lstRow1,lstRow2]
#objF = open("Todo.txt", 'w')
#objF.write(str(lstTable))
#objF.close()

#I couldn't load the data properly for step 2 so I manually typed into the text file.

#Step 2: Load data from the text file and fill into a dictionary
table = open("C:\_PythonClass\Module05Project\Todo.txt",'r')
dictRow = {}
lstTable = []
for line in table:
    x = line.split(",")
    a = x[0]
    b = x[1]
    c = len(b)-1
    b = b[0:c]
    dictRow = {'Task':a, 'Priority': b}
    lstTable.append(dictRow)
print(lstTable)

#Reference: https://www.youtube.com/watch?v=-Lu8VgYSkNQ

#Step 3 & 4: Add the new dictionary into a list table
while(True):
    strTask = input("Task: ")
    strPriority = input("Priority (high/low): ")
    dicNewRow1 = {"Task":strTask, "Priority":strPriority}
    lstTable.append(dicNewRow1)
    if(input("Type 'exit' to end?").lower() == "exit"): break
print(lstTable)

#Step 5 & 6: Add and Remove menu and save to text file
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        #continue
        print(lstTable)
        #if (input("Type 'exit' to end?").lower() == "exit"): break
    # Step 4 - Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        #continue
        while (True):
            strTask = input("Task: ")
            strPriority = input("Priority (high/low): ")
            dicNewRow1 = {"Task": strTask, "Priority": strPriority}
            lstTable.append(dicNewRow1)
            if (input("Type 'exit' to complete?").lower() == "exit"): break
        print(lstTable)
    # Step 5 - Remove a new item to the list/Table
    elif(strChoice == '3'):
        #continue
        row = int(input("Enter the number of row to delete (starting with 0): "))
        lstTable.remove(lstTable[row])
        print(lstTable)
    # Step 6 - Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        #continue
        objF = open("Todo.txt", 'a')
        objF.write(str(lstTable))
        objF.close()
        print("The following data was saved to a file: \n\r", lstTable)
        if (input("Type 'exit' to end?").lower() == "exit"): break
    elif (strChoice == '5'):
        print("Good bye!")
        break #and Exit the program














