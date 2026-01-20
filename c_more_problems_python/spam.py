# Write a function `spam(pairs)` that accepts a 2D list. Each inner list contains
# a word and a number. The function returns a string with each word repeated
# the specified number of times, separated by spaces.

def spam(pairs):
    result = []
    for word, count in pairs: # loop through each [word, count] pair
        for i in range(count): # for each pair, repeat the word count times and add to result
            result.append(word)
    return ' '.join(result) # join all words with spaces using ' '.join()


# Example usage:
array1 = [["hi", 3], ["bye", 2]]
print(spam(array1))  

array2 = [["cat", 1], ["dog", 2], ["bird", 4]]
print(spam(array2)) 

