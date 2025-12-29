def strings_to_lengths(strings):
    # Uses list comprehension to iterate through each string in strings.
    # Applies len() to get the length of each string.
    # Returns a new list with those lengths.
    return [len(s) for s in strings]


print(strings_to_lengths(["belly", "echo", "irony", "pickled"]))

print(strings_to_lengths(["on", "off", "handmade"]))
