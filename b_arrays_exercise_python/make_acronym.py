def make_acronym(sentence):
    # split the sentence into words
    words = sentence.split()
    # take the first character of each word and make it uppercase
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

print(make_acronym("New York"))
print(make_acronym("same stuff different day"))
print(make_acronym("Laugh out loud"))
print(make_acronym("don't over think stuff"))