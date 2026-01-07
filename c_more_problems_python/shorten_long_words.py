# Write a function `shorten_long_words(sentence)` that accepts a string and returns
# the same sentence where words longer than 4 characters have their vowels removed.

def shorten_long_words(sentence):
    vowels = set("aeiouAEIOU")
    result = []
    # split the sentence by spaces
    for token in sentence.split():
    # for each word/token: if its length is more than 4, remove vowels
        if len(token) > 4:
            token = "".join(ch for ch in token if ch not in vowels)
            result.append(token)
            # join everything back with spaces
    return " ".join(result)


# Example usage:
print(shorten_long_words("they are very noble people"))
print(shorten_long_words("stick with it"))
print(shorten_long_words("ballerina, you must have seen her"))  
