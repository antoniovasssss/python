# reading a file using with
with open("data2.txt","r") as file: # the with closes a file automatically and handles file safely
    content = file.read()
print(content)