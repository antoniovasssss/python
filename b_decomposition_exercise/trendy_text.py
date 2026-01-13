# Write a function `trendy_text` that accepts a sentence string as an argument.
# The function should return the sentence where the last vowel of every word
# is removed.

def remove_last_vowel(string):
    vowels = "aeiouAEIOU"
    for i in range(len(string) -1, -1, -1):
        if string[i] in vowels:
            return string[:i] + string[i + 1:]
    return string



def trendy_text(sentence):
    # split the sentence into individual words using split()
    words = sentence.split()
    trendy_words = []
    # loop through each word and apply remove_last_vowel to it
    for word in words:
        trendy_words.append(remove_last_vowel(word))
    # join the modified words back together with spaces using join()
    return ' '.join(trendy_words)
        

print(trendy_text("the concert will be epic"))

print(trendy_text("breakfast food is wonderful"))

print(trendy_text("the weather will improve hopefully"))

