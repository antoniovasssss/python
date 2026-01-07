# Write a function `remove_first_vowel(s)` that accepts a string and returns the string
# with its first vowel removed.

def remove_first_vowel(s):
    # define what counts as a vowel, both lowercase and uppercase
    vowels = "aeiouAEIOU"
    # loop through the string character by character
    for i, char in enumerate(s):
        # if the first vowel is found it's removed using string slicing
        if char in vowels:
            return s[:i] + s[i + 1:]
        # if the string contains no vowels the original string is returned
    return s

# Example usage:
print(remove_first_vowel("volcano")) 
print(remove_first_vowel("celery")) 
print(remove_first_vowel("juice")) 

