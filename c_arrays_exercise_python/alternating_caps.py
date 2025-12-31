def alternating_caps(sentence):
    # split the sentence into words
    words = sentence.split()

    # process each word: even index -> lowercase, odd index -> uppercase
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].lower()
        else:
            words[i] = words[i].upper()
    # join the words back into a sentence
    return " ".join(words)

print(alternating_caps("take them to school"))
print(alternating_caps("What did ThEy EAT before?"))