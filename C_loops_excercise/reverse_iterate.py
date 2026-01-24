# Write a function `reverse_iterate(text)` that prints each character of the string
# in reverse order. The function does not return a value, just prints.

def reverse_iterate(text):
    for char in reversed(text): # uses reversed(text) to iterate through the string backwards
        print(char) # prints each character one at a time


reverse_iterate("carrot")


reverse_iterate("box")