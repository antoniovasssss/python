total = 0 # Create an accumulator named total and start it at 0

# Because we want to build a running sum safely from zero
for i in range(1, 5): # Loop i over 1 2 3 4 since range stops before 5

# Because we want to add the integers from 1 through 4
    total += i # Add the current i into total
    print(total) # Show the running sum after this addition
    
print("grand total:", total) # After the loop print the final sum