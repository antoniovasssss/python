# Write a function `remove_last_vowel` that accepts a string as an argument.
# The function should return the string with its last vowel removed.
# Vowels are the letters: a, e, i, o, u

def remove_last_vowel(string):
    # define a string containing all vowels(both uppercase and lowercase)
    vowels = "aeiouAEIOU"
    # iterate through the string from right to left
    for i in range(len(string) -1, -1, -1):
        if string[i] in vowels:
            # remove the vowel by slicing before and after it
            return string[:i] + string[i + 1:]
    # if no vowel found, return the original string
    return string



print(remove_last_vowel("speaker"))
print(remove_last_vowel("trading"))
print(remove_last_vowel("thunder"))
print(remove_last_vowel("myth"))

