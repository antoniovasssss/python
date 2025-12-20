def multiplication_table(n: int) -> None:
    # loop i from 1 to 10
    for i in range(1, 11):
        # compute the product
        product = n * i
        # print one line per result
        print(product)

# example run to show output in the interactive window
multiplication_table(4)