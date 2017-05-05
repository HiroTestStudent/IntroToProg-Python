'''
Foundations of Programming (Python)
Module04_Assignment 
Hiroyuki Takechi
4/29/2017
'''

table = ('Name', 'Value'),

while(True):
    strName = input("Please enter the name of a household for this item: ")
    fltValue = input("Please enter the estimated value for this item: ")
    newrow = (strName,fltValue)
    table += newrow,

    print("Current entries in the table")
    for row in table:
        print(row)
    strContinue = input("Would you like to add new entries? (y/n): ")
    if (strContinue == 'y'):
        continue
    else:
        strSave = input("Do you want to save it to the file? (y/n): ")
        if (strSave == 'y'):
            fileSave = open("C:\_PythonClass\Module04Project\HomeInventory.txt", "a")
            for row in table:
                fileSave.write(row[0] + ',' + row[1] + "\n")
        break