# Write a function `make_acronym(sentence)` that accepts a string containing a sentence.
# The function should return a string containing the first character of each word in the sentence.

def make_acronym(sentence):
    words = sentence.split() # split the sentence into words
    return ''.join(word[0].upper() for word in words) # takes the first character of each word, converts to uppercase and joins them together


make_acronym("New York") 
make_acronym("same stuff different day")
make_acronym("Laugh out loud") 
make_acronym("don't over think stuff") 