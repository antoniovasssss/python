def censor_e(text):
    # Initialize an empty string to build the new result
    result = ""
    # Loop through each character in the input text
    for char in text:
        # If the character is 'e', replace it with '*'
        if char == 'e':
            result += '*'
        else:
            # Otherwise, keep the original character
            result += char
    # Return the final censored string
    return result

print(censor_e("speedy"))
print(censor_e("pending"))
print(censor_e("scene"))
print(censor_e("heat"))            