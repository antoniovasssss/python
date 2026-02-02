# Write a function `num_odds(numbers)` that accepts a list of numbers.
# The function should return the count of odd numbers in the list.

def num_odds(numbers):
    count = 0 # variable count that is initialized to 0
    for num in numbers: # a loop that iterates through each element in the numbers list
        if num % 2 != 0: # checks if the current number is odd
            count += 1 # if the number is odd, increment the count by 1
    return count # return the total count of odd numbers

num_odds([4, 7, 2, 5, 9]) 
num_odds([11, 31, 58, 99, 21, 60]) 
num_odds([100, 40, 4]) 