def five_multiples_of(n: int) -> None: # define a function that takes one number n
    for i in range(1, 6): # loop over 1 to 5 inclusive
        product = n * i # print the ith multiple of n
        print(product)
        
five_multiples_of(7) # prints 7 then 14 then 21 then 28 then 35