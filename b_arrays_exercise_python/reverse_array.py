# Write a function `reverse_array(arr)` that accepts a list as an argument.
# The function should return a list containing the elements of the original list in reverse order.

def reverse_array(arr):
    return arr[::-1] # slice notation with a step of -1 to create a reversed copy of the list

reverse_array(["zero", "one", "two", "three"])
reverse_array([7, 1, 8])