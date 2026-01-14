# Write a function `pick_perfect_squares` that accepts a list of numbers.
# The function should return a list containing only the perfect squares.
#
# A perfect square is a number that can be written as n * n.

def pick_perfect_squares(numbers):
    result = []
    # iterate through each number in the list
    for num in numbers:
        # check if the number is a non-negative(perfect squares can't be negative)
        if num >= 0:
            # calculate the square root of the number
            sqrt = num ** 0.5
            # check if the square root is a whole number by comparing it to its integer conversion
            if sqrt == int(sqrt):
                # if its a perfect square, add it to the result list
                result.append(num)
    return result



print(pick_perfect_squares([6,4,81,21,36]))

print(pick_perfect_squares([100,24,144]))

print(pick_perfect_squares([30,25]))
