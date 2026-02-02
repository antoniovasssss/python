# Write a function `stay_positive(numbers)` that accepts a list of numbers.
# The function should return a new list containing only the positive numbers.

def stay_positive(numbers):
    return [num for num in numbers if num > 0]

stay_positive([10, -4, 3, 6]) 
stay_positive([-5, 11, -40, 30.3, -2])
stay_positive([-11, -30])