# Write a function `number_range(min_val, max_val, step)` that accepts three numbers as arguments.
# The function should return a list of numbers starting from min_val to max_val (inclusive),
# incremented by step.

def number_range(min_val, max_val, step):
    result = [] # create an empty list to store the numbers 
    current = min_val # start with current set to min_val

    while current <= max_val: # while current is less than or equal to max_val...
        result.append(current) # add it to the result list
        current += step # increment current by step

    return result # return the complete list


number_range(10, 40, 5)
number_range(14, 24, 3) 
number_range(8, 35, 6)