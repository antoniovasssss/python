# Write a function `divisible_range(min_val, max_val, num)` that prints all numbers
# between min_val and max_val (exclusive) that are divisible by num.
# The function does not return a value, just prints.

def divisible_range(min_val, max_val, num):
    for i in range(min_val, max_val): # iterates through all numbers from min_val to max_val
        if i % num == 0: # checks if each number is divisible by num using the modulo operator(%)
            print(i) # prints the number if the remainer is 0 (meaning it's divisible)


divisible_range(17, 40, 9)


divisible_range(10, 24, 4)