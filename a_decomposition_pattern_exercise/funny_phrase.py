def double_vowel(string):
    vowels = "aeiouAEIOU"
    result = " "
    for char in string:
        if char in vowels:
            result += char * 2
        else:
            result += char
    
    return result

def funny_phrase(sentence):
    # splitting the sentence into a list of words
    words = sentence.split()
    # iterating through each word with its index
    for i in range(len(words)):
        # for words at odd indices(1, 3, 5, etc.) applying the double_vowel function
        if i % 2 == 1:
            words[i] = double_vowel(words[i])
    # joining the words back together with spaces
    return " ".join(words)


print(funny_phrase("she dreamed of being a runner"))

print(funny_phrase("park near the stoplight"))

print(funny_phrase("we need many gardeners"))

