def word_count(sentence, target_words):
    # split the sentence into words
    words = sentence.split()
    # count how many words are in target_words
    count = sum(1 for word in words if word in target_words)
    return count

print(word_count("open the window please", ["please", "open", "sorry"]))
print(word_count("drive to the cinema", ["the", "drive"]))
print(word_count("can I have that can", ["can", "I"]))