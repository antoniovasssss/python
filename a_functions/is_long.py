def is_long(text):
    return len(text) > 5 # the len() function returns the number of characters in a string.
    # The expression len(text) > 5 checks if the length is greater than 5, returning True if it is, and False otherwise

print(is_long("pie"))           # False
print(is_long("kite"))          # False
print(is_long("kitty"))         # False
print(is_long("telescope"))     # True
print(is_long("thermometer"))   # True
print(is_long("restaurant"))    # True