def object_add(obj1, obj2):
    # create a copy of the first dictionary to avoid modifying the original
    result = obj1.copy()
    # iterate through each key-value pair in the second dictionary
    for key, value in obj2.items():
        # use result.get... to get the existing value(or 0 if the key doesn't exist) and add the new value
        result[key] = result.get(key, 0) + value
    # return the merged result
    return result

obj1 = {"x":3,"y":10 }
obj2 = {"y":2,"x":1 }

print(object_add(obj1, obj2))


obj3 = {"a":3,"b":2,"c": -1 }
obj4 = {"b":5,"c":1,"e":4 }

print(object_add(obj3, obj4))

