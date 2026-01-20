# Write a function `remove_vowels(s)` that accepts a string and returns a new string
# with all vowels removed (a, e, i, o, u).

def remove_vowels(s):
    vowels = "aeiouAEIOU" # define all vowels
    result = ""
    for char in s: # loop through each character in the string 
        if char not in vowels: # if the character is not a vowel, add it to the result
            result += char
    return result # return the result string


print(remove_vowels("jello"))  
print(remove_vowels("sensitivity")) 
print(remove_vowels("cellar door"))