
# Write a function `bleep_vowels(text)` that accepts a string and returns
# a new string where all vowels (a, e, i, o, u) are replaced with '*'.

def bleep_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char in vowels:
            result += '*'
        else:
            result += char
    return result


bleep_vowels("skateboard") 
bleep_vowels("slipper")
bleep_vowels("range")
bleep_vowels("brisk morning")

