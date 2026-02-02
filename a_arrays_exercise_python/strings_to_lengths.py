# Write a function `strings_to_lengths(strings)` that accepts a list of strings.
# The function should return a new list containing the lengths of each string.

def strings_to_lengths(strings):
    return [len(string) for string in strings]

strings_to_lengths(["belly", "echo", "irony", "pickled"]) 
strings_to_lengths(["on", "off", "handmade"]) 