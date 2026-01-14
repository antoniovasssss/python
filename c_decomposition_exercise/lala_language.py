# Write a function `lala_language` that accepts a sentence string as an argument.
# The function should return a new sentence where words longer than 3 characters
# are modified.
#
# Modified words should have each vowel followed by 'l' and the same vowel again.
# See the examples below.

def lala_language(sentence):
    # define vowels(both uppercase and lowercase)
    vowels = "aeiouAEIOU"
    # split the sentence into individual words
    words = sentence.split()
    result = []
    # for each word 
    for word in words:
        # if its longer than 3 characters, iterate through each character
        if len(word) > 3:
            modified_word = ''
            for char in word:
                # add the character to the modified word
                modified_word += char
                # if the character is a vowel, append 'l' + the lowercase version of that vowel
                # if its 3 characters or less, keep it unchanged
                if char in vowels:
                    modified_word += 'l' + char.lower()
            result.append(modified_word)
        else:
            result.append(word)
    # join all words back together with spaces
    return ' '.join(result)

print(lala_language('this is pretty strange'))

print(lala_language('can you speak our language'))

# The function correctly handles the examples:

# 'this' (4 chars) → 'thilis' (i becomes ili)
# 'pretty' (6 chars) → 'preletty' (e becomes ele)
# 'strange' (7 chars) → 'stralangele' (a becomes ala, e becomes ele)