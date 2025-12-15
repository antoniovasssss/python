def in_range(min_val: float, max_val: float, n: float) -> bool:
    # If the user passed the bounds in reverse order then fix them
    if min_val > max_val:  # compare the two bounds
        min_val, max_val = max_val, min_val
    return min_val <= n <= max_val # swap so min_val is the smaller

print(in_range(5, 13, 8))        # True  because 8 is between 5 and 13
print(in_range(5, 13, 29))       # False because 29 is above 13
print(in_range(100, 125, 100))   # True  because equality at the lower bound counts
print(in_range(100, 125, 99))    # False because 99 is below 100
print(in_range(45, 45, 45))      # True  because both bounds equal and n equals them
print(in_range(45, 45, 46))      # False because 46 is above 45
print(in_range(13, 5, 8))        # True  because the swap fixes reversed bounds