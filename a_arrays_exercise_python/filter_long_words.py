def filter_long_words(words):
    # Uses list comprehension to iterate through words.
    # Keeps only words where len(word) < 5.
    return [word for word in words if len(word) < 5]

print(filter_long_words(["kale", "cat", "retro", "axe", "heirloom"]))
print(filter_long_words(["disrupt", "pour", "trade", "pic"]))
