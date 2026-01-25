# Write a function `fizz_buzz(max_num)` that prints all numbers <= max_num
# that are divisible by 3 or 5 but not both.
# The function does not return a value, just prints.

def fizz_buzz(max_num):
    for i in range(1, max_num + 1): # loops through numbers from 1 to max_num
        if (i % 3 == 0 or i % 5 == 0) and not (i % 3 == 0 and i % 5 == 0): # checks if the number is divisible by 3 or 5 but not both
            print(i) # prints the number if it meets the condition


fizz_buzz(18)

fizz_buzz(33)