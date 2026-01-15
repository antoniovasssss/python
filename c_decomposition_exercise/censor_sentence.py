# Write a function `censor_sentence(sentence, target_words)` that accepts:
# - a sentence string
# - a list of target words
#
# The function should return a new sentence where each target word
# is replaced with '*' characters of the same length.

def censor_sentence(sentence, target_words):
    # splitting the sentence into individual words
    words = sentence.split()
    censored_words = []
    # checking each word against the target words list
    for word in words:
        if word in target_words:
            # if a word matches, replacing it with asterisks of the same length
            censored_words.append("*" * len(word))
        else:
            censored_words.append(word)

    # joining all the words back together with spaces
    return ' '.join(censored_words)
    
print(censor_sentence('where the heck is my celery', ['heck','celery']))

print(censor_sentence('why you little sweetheart', ['sweetheart','salad']))
