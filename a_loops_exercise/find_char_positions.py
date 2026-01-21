# Write a function that prints all **indexes** where a character appears in a string.

def find_char_positions(text, char):
    for i in range(len(text)): # this generates indices from 0 to the length of the string minus i, for each index i, we check...
        if text[i] == char: # if text[i] equals the character we're searching for, if it matches...
            print(i) # we print print that index



find_char_positions("banana", "a")