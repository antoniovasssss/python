# Write a function `remove_capitals(text)` that returns a new string with all
# capital letters removed.

def remove_capitals(text):
    result = "" # creates an empty string result to store characters we want to keep
    for char in text: # loops through each character in text
        if not char.isupper(): # uses char.isupper() to check if the character is uppercase, if it's not uppercase...
            result += char # adds it to result
    return result # returns the new string with all capitals removed

remove_capitals("fOrEver")     
remove_capitals("raiNCoat")    
remove_capitals("cElLAr Door")

