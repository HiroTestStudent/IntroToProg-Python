'''
Create a new program that asks the user for the name of a household
item, and then asks for its estimated value. Store, both pieces of data in
a text file called, HomeInventory.txt
'''
#open the file
objFH = open("C:\_PythonClass\Module03Project\HomeInventory.txt", "w")
#start a loop that will process data until the user types exit
while(True):
    #Get the name of a household item
    data1 = input("Enter the name of a household:")
    #Get the estimated value
    data2 = float(input("Enter its estimated value:"))
    #Write answer to the file
    objFH.write(data1 + " " + "$" + str(data2) + "\n")
    #Ask the use if they want to continue
    if(input("Type 'exit' to quit this program:")): break
#Close the file
objFH.close()