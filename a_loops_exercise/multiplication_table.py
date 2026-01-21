# Print the multiplication table of a number up to 10.

def multiplication_table(n):
    for i in range(1, 11): # loop through numbers 1 to 10 using range(1, 11)
        print(n * i) # multiply n by each number and print the result

multiplication_table(4)

# Prints:
# 4    (4 × 1)
# 8    (4 × 2)
# 12   (4 × 3)
# 16   (4 × 4)
# 20   (4 × 5)
# 24   (4 × 6)
# 28   (4 × 7)
# 32   (4 × 8)
# 36   (4 × 9)
# 40   (4 × 10)