def raise_power(base, exponent):
    # Initialize result as 1 because any number raised to 0 is 1
    result = 1
    
    # Loop 'exponent' times to multiply base repeatedly
    for _ in range(exponent):
        # Multiply current result by base in each iteration
        result *= base
    
    # After the loop, result holds base^exponent
    return result

# Examples:
print(raise_power(2, 5))  
print(raise_power(4, 3))   
print(raise_power(10, 4))  
print(raise_power(7, 2))   

