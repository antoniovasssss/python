def double_vowel(string):
    # defining a string containing all vowels (both lowercase and uppercase)
    vowels = "aeiouAEIOU"
    result = " "
    # iterating through each character in the input string
    for char in string:
        if char in vowels:
            result += char * 2
        # if its not a vowel, adding it once
        else:
            result += char
    # returning the final result
    return result


print(double_vowel("runner"))

print(double_vowel("stoplight"))

print(double_vowel("gardener"))

