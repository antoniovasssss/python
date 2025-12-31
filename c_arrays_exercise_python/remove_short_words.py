def remove_short_words(sentence):
    # split the sentence into words
    words = sentence.split()

    # keep only words with length >= 4
    filtered_words = [word for word in words if len(word) >= 4]
    
    # join back into a sentence
    return " ".join(filtered_words)

print(remove_short_words("knock on the door will you"))
print(remove_short_words("a terrible plan"))
print(remove_short_words("run faster that way"))