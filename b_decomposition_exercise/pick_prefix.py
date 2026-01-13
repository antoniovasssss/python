# Write a function `pick_prefix(strings, prefix)` that accepts:
# - a list of strings
# - a prefix string
#
# The function should return a list of words that begin with the prefix.
def pick_prefix(strings, prefix):
    # create an empty list to store the results
    result = []
    # loop through each string in the input list
    for string in strings:
        # check if the string starts with the given prefix using the startswith() method
        if string.startswith(prefix):
            # if it does, add it to the result list
            result.append(string)
    # return the result list
    return result
        

print(pick_prefix(['connect','company','concert','cram'],'con'))


print(pick_prefix(['miner','mistake','misspeak','moose','mission'],'mis'))

