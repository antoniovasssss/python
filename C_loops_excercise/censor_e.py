# Write a function `censor_e(text)` that returns a new string where all 'e' characters
# are replaced with '*'.

def censor_e(text):
    result = "" # create an empty string result to build our answer
    for char in text: # goes through each character in text
        if char == 'e': # if the character is 'e'
            result += '*' # adds a '*' to result
        else: # if the character is anything else, adds the original character to result
            result += char
    return result # returns the new string with all 'e's replaced


censor_e("speedy") 
censor_e("pending") 
censor_e("scene")   
censor_e("heat")    