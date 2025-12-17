def sum_upto(n):
    # Define a function named sum_upto that takes one argument n
    if n < 1:
    # Guard for nonpositive input since there are no numbers from 1 to n
        return 0 # Return 0 when n is less than 1
    return n * (n + 1) // 2 # Use the arithmetic series formula n(n+1)/2 with integer division

print(sum_upto(5)) # Call the function with n = 5 then print 15
print(sum_upto(10)) # Call the function with n = 10 then print 55