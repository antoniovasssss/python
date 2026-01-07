# a functions that accepts two dictionaries, a key string
def key_pair(dict1, dict2, key):
    # return a list containing the values for the given key from both dictionaries
    return [dict1[key], dict2[key]]

cat1 = {"name":"jinkee", "breed": "calico"}
cat2 = {"name":"garfield", "breed": "red tabby"}

print(key_pair(cat1, cat2, "breed"))
print(key_pair(cat1, cat2, "name"))
    
