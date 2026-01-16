def exclaim(s):
    capitalized = s.upper()
    return capitalized + "!!"


result = exclaim("potato") # converts "potato" to uppercase ("POTATO") and adds "!!" to the end
print(result) # outputs POTATO!!
print(len(result)) # the string POTATO!! has 6 letters + 2 exclamation marks = 8 characters
print(result[0]) # the first character [index 0] is P 
print(result[-1]) # the last character (index -1, counting from the end) is !
