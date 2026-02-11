# writing to a file using with
with open("output.txt", "w") as file: # using with, once this block ends, the file is closed automatically
    file.write("Hello Python\n")
    file.write("Using with statement")