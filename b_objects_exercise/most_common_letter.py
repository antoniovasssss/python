def most_common_letter(string):
    # creates a dictionary to count each character in the string
    counts = {}
    
    for char in string:
        counts[char] = counts.get(char, 0) + 1

    max_char = None
    max_count = 0
    # loops through the counts to find the character with the highest count
    for char, count in counts.items():
        if count > max_count:
            max_char = char
            max_count = count
    # returns that character
    return max_char

print(most_common_letter("building"))

print(most_common_letter("shoestring"))

print(most_common_letter("preparedness"))