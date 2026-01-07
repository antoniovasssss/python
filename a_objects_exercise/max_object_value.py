def max_object_value(dictionary):
    # init variables to track the maximum key and value
    max_key = None
    max_value = None
    # loops through each key-value pair in the dictionary
    for key, value in dictionary.items():
        # updates the maximum whenever it finds a larger value
        if max_value is None or value > max_value:
            max_key = key
            max_value = value
    # returns a list with the key and value
    return [max_key, max_value]

print(max_object_value({"a": 5, "b": 2, "c": 6, "d": 7, "e": 4}))

print(max_object_value({"lychee": 11, "rambutan": 13, "papaya": 9}))
