def total_product(matrix):
    product = 1
    for row in matrix:
        for num in row:
            product *= num
    return product

array1 = [[3, 5, 2], [6, 2]]
array2 = [[4, 6], [2, 3], [1, 2]]

print(total_product(array1))
print(total_product(array2))