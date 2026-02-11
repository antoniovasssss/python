file = open("data.txt", "r") # opens the file 
content = file.read() # reads all the content, stores it in a variable
print(content) # prints it
file.close() # closes the file to prevent data corruption

