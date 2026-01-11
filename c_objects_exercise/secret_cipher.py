def secret_cipher(string, cipher_map):
    # start with an empty result string
    result = ""
    # iterate through each character in the input string
    for char in string:
        # use cipher_map.get... to look up the character in the dictionary, defaulting to "?" if not found
        # append the mapped character or "?" to the result
        result += cipher_map.get(char, "?")
    # return the completed cipher string
    return result

print(secret_cipher("jello", {"j":"r","l":"s","e":"i" }))

print(secret_cipher("lantern", {"e":"o","l":"p","n":"m","r":"j" }))

