# Write a function `alternating_caps(sentence)` that accepts a string containing a sentence.
# The function should return the sentence where words alternate between lowercase and uppercase.

def alternating_caps(sentence):
    words = sentence.split() # split the sentence into a list of words
    result = [] # create an empty list to store the modified words

    for i in range(len(words)): # loop through each word using its index
        if i % 2 == 0: # if the index is even (0, 2, 4...)
            result.append(words[i].lower()) # then convert the word to lowercase
        else: # else if odd (1, 3, 5...)
            result.append(words[i].upper()) # convert the word to uppercase

    return ' '.join(result) # join the words back together with spaces


alternating_caps("take them to school") 
alternating_caps("What did ThEy EAT before?")