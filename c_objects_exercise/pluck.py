def pluck(dictionary, keys):
    # creates an empty dictionary result
    result = {}
    # iterates through each key in the provided list
    for key in keys:
        # if the key exists in the original dictionary, add that key-value pair to result
        if key in keys:
            result[key] = dictionary[key]
    # return the new dictionary containing only the specified keys
    return result



print(pluck(
    {"name":"Fido","color":"Brown","breed":"German Shepherd" },
    ["name","breed"]
))
# { "name": "Fido", "breed": "German Shepherd" }

print(pluck(
    {"make":"Tesla","mpg":93,"model":"Model X","color":"white" },
    ["make","model"]
))
# { "make": "Tesla", "model": "Model X" }

