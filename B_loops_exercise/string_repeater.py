# Write a function `string_repeater(text, n)` that returns a new string
# consisting of `text` repeated `n` times.

def string_repeater(text, n):
    result = "" # initializes an empty string result
    for i in range(n): # then loops n times
        result += text # adding text to the result each time 
    return result # the concatenated string is returned

# Example:
string_repeater("q", 4)  #-> 'qqqq'
string_repeater("go", 2) #-> 'gogo'
string_repeater("tac", 3) #-> 'tactactac'