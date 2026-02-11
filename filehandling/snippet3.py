name = input("Enter student name: ")

file = open("students.txt", "a")
file.write(name + "\n")
file.close()