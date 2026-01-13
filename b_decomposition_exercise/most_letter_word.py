# Write a function `most_letter_word(sentence, char)` that accepts:
# - a sentence string
# - a single character
#
# The function should return the word in the sentence that contains the
# character the greatest number of times.
#
# You can assume the sentence contains at least one word.
# If there is a tie, return the word that appears first in the sentence.

def most_letter_word(sentence, char):
    # split the sentence into a list of words
    words = sentence.split()
    # initialize max_count to 0 and result_word to the first word
    max_count = 0
    result_word = words[0]
    # loop through each word in the sentence
    for word in words:
        # count how many times the character appears in each word using the count() method
        count = word.count(char)
        # if the current word has more occurences than the previous maximum, update both max_count and result_word
        if count > max_count:
            max_count = count
            result_word = word
    # return the word with the most occurrences
    return result_word


print(most_letter_word(
'she received an award for excellence in science','e'
))

print(most_letter_word(
'she received an award for excellence in science','a'
))

print(most_letter_word(
'I hope sophomore year comes soon','o'
))

print(most_letter_word(
'I hope sophomore year comes soon','s'
))
