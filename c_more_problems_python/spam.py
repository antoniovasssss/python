def spam(pairs):
    return " ".join(
        word
        for word, count in pairs
        for _ in range(count)
    )

array1 = [["hi", 3], ["bye", 2]]
print(spam(array1))

array2 = [["cat", 1], ["dog", 2], ["bird", 4]]
print(spam(array2))