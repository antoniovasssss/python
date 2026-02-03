# Write a function `word_count(sentence, target_words)` that accepts a sentence string and a list of target words.
# The function should return a count of how many words in the sentence are also in target_words.

def word_count(sentence, target_words):
    words = sentence.split() # split the sentence into a list of individual words
    count = 0 # initialize a counter to track matches
    for word in words:
        if word in target_words: # check if each word from the sentence is in target_words
            count += 1 # if it is, increment the counter
    return count # return the total count


word_count("open the window please", ["please", "open", "sorry"]) 
word_count("drive to the cinema", ["the", "driver"]) 
word_count("can I have that can", ["can", "I"]) 
