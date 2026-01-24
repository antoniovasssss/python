# Write a function `raise_power(base, exponent)` that returns the result of
# base raised to the exponent using loops (do not use ** operator or math.pow).

def raise_power(base, exponent):
    result = 1 # starts with result = 1 (since multiplying by 1 doesn't change the value)
    for i in range(exponent): # loops exponent times
        result *= base # each time through the loop, multiplies result by base
    return result # returns the final result


raise_power(2, 5) 
raise_power(4, 3) 
raise_power(10, 4)
raise_power(7, 2)  