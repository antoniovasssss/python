# Write a function `five_multiples_of(n)` that prints the first five multiples of n.
# The function does not return a value, just prints.

# Example:

def five_multiples_of(n):
    for i in range(1, 6): # the function uses a loop that iterates from 1 to 5, 6(exclusive), multiplying n by each number and printing the result
        print(n * i) # each multiple is printed on its own line

five_multiples_of(7)