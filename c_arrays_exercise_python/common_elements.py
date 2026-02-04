# Write a function `common_elements(arr1, arr2)` that accepts two lists as arguments.
# The function should return a new list containing the elements that are found in both input lists.
# The order of elements in the output list doesn't matter.

def common_elements(arr1, arr2):
    result = [] # create an empty list to store common elements

    for element in arr1: # loop through each element in the first list 
        if element in arr2 and element not in result: # check if the element exists in the second list AND hasn't been added to result yet (to avoid duplicates)
            result.append(element) # if both conditions are true , add or append it to the result list

    return result # return the list of common elements


common_elements(["a", "c", "d", "b"], ["b", "a", "y"])
common_elements([4, 7], [32, 7, 1, 4])