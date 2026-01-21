# Write `sum_of_range(n)`

# Print the sum of numbers from 1 to n.

def sum_of_range(n):
    total = 0 # initialize total to 0
    for i in range(1, n + 1): # loop through numbers from 1 to n (inclusive) just says go from 1 to n(5)
        total += i # add each number to total
    print(total) # print the final sum

sum_of_range(5)

# When we call sum_of_range(5), we're adding all numbers from 1 to 5:

# 1 + 2 + 3 + 4 + 5 = ?

# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15