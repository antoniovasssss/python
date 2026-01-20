# Write a function `remove_first_vowel(s)` that accepts a string and returns the string
# with its first vowel removed.

def remove_first_vowel(s):
    vowels = "aeiouAEIOU" # define all vowels
    for i in range(len(s)): # loop through each character by index
        if s[i] in vowels:
            return s[:i] + s[i+1:] # everything before & after the vowel
    return s # if no vowel is found, return the original string


# Example usage:
print(remove_first_vowel("volcano"))  
print(remove_first_vowel("celery")) 
print(remove_first_vowel("juice"))
