def your_average_function(numbers):
    # check if the list is empty
    if not numbers:
        # if there is no num return None
        return None
    # calculate the average
    return sum(numbers) / len(numbers)

print(your_average_function([5, 2, 7, 24]))
print(your_average_function([100, 6]))
print(your_average_function([31, 32, 40, 12, 33]))
print(your_average_function([]))