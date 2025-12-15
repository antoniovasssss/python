def average_of_four(a, b, c, d):
    # Ensure inputs are numbers for safety
    for x in (a, b, c, d):
        if not isinstance(x, (int, float)):
            raise TypeError("All inputs must be int or float")
    # Sum the four values
    total = a + b + c + d

    avg = total / 4

    return avg

print(average_of_four(10, 4, 12, 3))   # 7.25
print(average_of_four(-20, 50, 4, 21)) # 13.75
print(average_of_four(5, 5, 3, 7))     # 5.0