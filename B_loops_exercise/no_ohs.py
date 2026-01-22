# Write a function `no_ohs(text)` that prints each character of the string except 'o'.
# The function does not return a value, just prints.

def no_ohs(text):
    for char in text: # for each char...
        if char != 'o': # it checks if its not equal to 'o', if the char is anything other than 'o'...
            print(char) # it prints it on its own line

# Example:
no_ohs("code")