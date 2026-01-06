def remove_vowels(s):
    # we define a string of vowels to remove
    vowels = "aeiou"
    result = ""
    # we loop through each character in the input string
    for char in s:
        if char not in vowels:
            result += char
    return result

print(remove_vowels("jello"))
print(remove_vowels("sensitivity"))
print(remove_vowels("cellar door"))