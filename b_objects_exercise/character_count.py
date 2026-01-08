def character_count(str):
    # create an empty dictionary called counts
    counts = {}
    # loops through each character in the string
    for char in str:
        # if the character is already in the dictionary, increments its count
        if char in counts:
            # if its a new character, adds it to the dictionary with a count of 1
            counts[char] += 1
        else:
            counts[char] = 1
    # returns the dictionary with all character counts
    return counts


print(character_count("evening"))

print(character_count("mississippi"))

print(character_count("chili"))

