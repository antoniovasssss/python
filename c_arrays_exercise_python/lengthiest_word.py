def lengthiest_word(sentence):
    # split the sentence into words
    words = sentence.split()

    # initialize variables to track the longest word and its length
    longest_word = ""
    max_length = 0
    
    # iterate through the words
    for word in words:
        if len(word) >= max_length: # Use >= to prioritize later words in case of a tie
            longest_word = word
            max_length = len(word)
    return longest_word

print(lengthiest_word("I am pretty hungary"))
print(lengthiest_word("we should think outside of the box"))
print(lengthiest_word("down the rabbit hole"))
print(lengthiest_word("simmer down"))     