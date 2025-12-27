def product_up_to(max_num):
    product = 1
    for i  in range(1, max_num + 1):
        product *= i
    return product

print(product_up_to(4))
print(product_up_to(5))
print(product_up_to(7))