# Write a function `sum_up_to(max_num)` that returns the sum of all whole numbers
# from 1 to max_num inclusive.

def sum_up_to(max_num):
    total = 0 # initializes a total variable to 0
    for i in range(1, max_num + 1): # loops through all numbers from 1 to max_num(inclusive)
        total += i # adding each number to the total
    return total # returns it to the sum


sum_up_to(4)  
sum_up_to(5) 
sum_up_to(2) 

# sum_up_to(4) → 10

# We add: 1 + 2 + 3 + 4 = 10
# sum_up_to(5) → 15

# We add: 1 + 2 + 3 + 4 + 5 = 15
# sum_up_to(2) → 3

# We add: 1 + 2 = 3