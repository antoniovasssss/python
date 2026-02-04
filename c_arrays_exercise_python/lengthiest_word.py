# Write a function `lengthiest_word(sentence)` that accepts a string containing a sentence.
# The function should return the longest word in the sentence.
# If there is a tie, return the word that appears later in the sentence.

def lengthiest_word(sentence):
    words = sentence.split() # split the sentence into a list of words using split()
    longest = words[0] # initialize longest with the first word

    for word in words: # iterate through each word in the list
        if len(word) >= len(longest): # using >= ensures that if a word has the same length as the current longest, it replaces it 
            longest = word

    return longest # return the longest word found


lengthiest_word("I am pretty hungry") 
lengthiest_word("we should think outside of the box")
lengthiest_word("down the rabbit hole") 
lengthiest_word("simmer down")