def letter_map(string, mapping):
    # create an empty string called result
    result = ""
    # loops through each character in the input string
    for char in string:
        # if the char exists as a key in the mapping dictionary, adds the mapped value to the result
        if char in mapping:
            # if the char doesn't exist in the mapping, adds the original char to the result
            result += mapping[char]
        else:
            result += char
    # returns the transformed string
    return result

print(letter_map("symbolic", {"y": "i", "o": "a", "c": "k"}))


print(letter_map("colossal", {"o": "x", "s": "p"}))


print(letter_map("miniscule", {"u": "t", "i": "f", "e": "q"}))
