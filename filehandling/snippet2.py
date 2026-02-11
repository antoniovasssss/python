file =open("output.txt","w") # create file output.txt
file.write("Hello Python\n") # write data into it
file.write("File handling is useful")
file.close() # close the file

# Appending data to a file
file =open("output.txt","a") # using a to append data
file.write("\nLearning step by step") # adds the new data without removing the old data
file.close() # closes the file

