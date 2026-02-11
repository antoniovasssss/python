# string comprehension
word = "python"
letters = [ch.upper() for ch in word] # puts the characters in the string in uppercase and loops through each character in the string
print(letters)


# Project(Test)
# 1. Create a list of squares of even numbers from 1 to 20
squares_of_evens = [i**2 for i in range(1,21) if i % 2 == 0]
print("Squares of even numbers:", squares_of_evens)

# 2. Convert a list into a set using comprehension
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = {x for x in my_list}
print("Set from list:", my_set)

# 3. Create a dictionary of numbers and their cubes
cubes_dict = {num: num**3 for num in range(1,6)}
print("Numbers and cubes:", cubes_dict)