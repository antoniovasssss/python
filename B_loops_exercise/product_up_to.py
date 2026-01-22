# Write a function `product_up_to(max_num)` that returns the product of all numbers
# from 1 to max_num inclusive. (1*2*3*...*max_num)

def product_up_to(max_num):
    product = 1 # initializes a product variable to 1(not 0, since multiplying by 0 would give 0)
    for i in range(1, max_num + 1): # then it loops through all numbers from 1 to max_num
        product *= i # multiplying each number into the product
    return product # product is returned

# Example:
product_up_to(4)
product_up_to(5)
product_up_to(7) 

# product_up_to(4): 1 × 2 × 3 × 4 = 24
# product_up_to(5): 1 × 2 × 3 × 4 × 5 = 120
# product_up_to(7): 1 × 2 × 3 × 4 × 5 × 6 × 7 = 5040