# Write a function `maximum(numbers)` that accepts a list of numbers.
# The function should return the largest number in the list.
# If the list is empty, return None.

def maximum(numbers):
    if not numbers: # checks if the list is empty 
        return None # return None since theres no maxnum to find
    
    max_num = numbers[0] # variable max_num to keep track of the largest number we've seen, by assuming the first number is the largest numbers[0]
    for num in numbers: # loop through each number in list
        if num > max_num: # check is this number bigger than our current max_num?
            max_num = num # if no we update max_num to be this new larger number 

    return max_num # holds the largest value, so we return it

maximum([5, 6, 3, 7]) 
maximum([17, 15, 19, 11, 2]) 
maximum([])