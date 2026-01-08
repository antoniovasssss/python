def word_replace(sentence, mapping):
    # splits the sentence into a list of words using split()
    words = sentence.split()
    # creates an empty list called result
    result = []
    # loops through each word
    for word in words:
        # if the word exits as a key in the mapping dictionary, adds the mapped value to the result
        if word in mapping:
            result.append(mapping[word])
        else:
            # if the word doesn't exist in the mapping, add the original word to the result
            result.append(word)
    # joins all the words back together with spaces using join()
    return " ".join(result)

print(word_replace(
    "I never take naps during the day",
    {"never": "always", "day": "weekend"}
))

print(word_replace(
    "the park is closed",
    {"closed": "open", "the": "a"}
))

print(word_replace(
    "I do what I want",
    {"I": "we", "cat": "dog"}
))

