# Write a function `remove_short_words(sentence)` that accepts a string containing a sentence.
# The function should return a new sentence where all words shorter than 4 characters are removed.

def remove_short_words(sentence):
    words = sentence.split() # split the sentence into a list of words 
    result = [] # create an empty list to store words that are long enough 

    for word in words: # loop through each word
        if len(word) >= 4: # if the word has 4 or more characters..
            result.append(word) # add it to the result list

    return ' '.join(result) # join the filtered words back together with spaces




remove_short_words("knock on the door will you") 
remove_short_words("a terrible plan")
remove_short_words("run faster that way")