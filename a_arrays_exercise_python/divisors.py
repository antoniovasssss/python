# Write a function `divisors(num)` that accepts a number.
# The function should return a list containing all positive numbers that divide num exactly.

def divisors(num):
    return [i for i in range(1, num + 1) if num % i == 0] # creates a list of all numbers from 1 to num that divide num evenly (with no remainder)

divisors(15) 
divisors(7) 
divisors(24) 

