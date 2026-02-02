# Write a function `your_average_function(numbers)` that accepts a list of numbers.
# The function should return the average of all elements in the list.
# If the list is empty, the function should return None.

def your_average_function(numbers):
    if len(numbers) == 0: # checks if the list is empty
        return None # returns None if it is
    return sum(numbers) / len(numbers) # calculates the average by dividing the sum by the count of numbers

your_average_function([5, 2, 7, 24]) 
your_average_function([100, 6]) 
your_average_function([31, 32, 40, 12, 33]) 
your_average_function([]) 

