def maximum(numbers):
    # check if the list is empty
    if not numbers:
        return None
    # return the largest number using max()
    return max(numbers)

print(maximum([4, 6, 3, 7]))
print(maximum([17, 15, 19, 11, 2]))
print(maximum([]))
