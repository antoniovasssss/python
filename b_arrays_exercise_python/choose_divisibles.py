# Write a function `choose_divisibles(numbers, target)` that accepts a list of numbers and a target number.
# The function should return a new list containing only the elements divisible by the target.

def choose_divisibles(numbers, target):
    return [num for num in numbers if num % target == 0] # the modulo operator (%) checks if a number is divisible by the target, theres no remainder (== 0), meaning its evenly divisible


choose_divisibles([40, 7, 22, 20, 24], 4) 
choose_divisibles([9, 33, 8, 17], 3) 
choose_divisibles([4, 25, 1000], 10) 

