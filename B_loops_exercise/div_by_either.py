# Write a function `div_by_either(num1, num2, max_num)` that prints all positive numbers
# less than max_num that are divisible by num1 or num2.
# The function does not return a value, just prints.

def div_by_either(num1, num2, max_num):
    for i in range(1, max_num): # loops through all positive numbers from 1 up to max_num. For each number i
        if i % num1 == 0 or i % num2 == 0: # it checks if its divisible by num1 OR divisible by num2 using the modulo operator %
            print(i) # it prints the number

# Example:
div_by_either(4, 3, 16)

# Let's verify with the example div_by_either(4, 3, 16):

# 3: divisible by 3 ✓
# 4: divisible by 4 ✓
# 6: divisible by 3 ✓
# 8: divisible by 4 ✓
# 9: divisible by 3 ✓
# 12: divisible by both 3 and 4 ✓
# 15: divisible by 3 ✓