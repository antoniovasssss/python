def bleep_vowels(text):
    # We define a string vowels containing all lowercase and uppercase vowels.
    vowels = "aeiouAEIOU"
    # If char is a vowel, replace it with '*'.
    return ''.join('*' if char in vowels else char for char in text)

bleep_vowels("skateboard")
bleep_vowels("skipper")
bleep_vowels("range")
bleep_vowels("brisk morning")