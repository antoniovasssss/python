def sum_of_range(n): # define a function that takes n
    if n < 1: # guard for non positive input
        return 0 # return 0 so the loop is skipped
        
    total = 0 # start an accumulator at 0
    
    for i in range(1, n + 1): # loop from 1 to n inclusive
        total += i # add each i to total
    return total # return the sum
    
print(sum_of_range(5)) # call the function and print the result