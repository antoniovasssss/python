def is_div_by_4(num):
    return num % 4 == 0

# quick checks
print(is_div_by_4(8))    # True, because 8 % 4 is 0
print(is_div_by_4(12))   # True, because 12 % 4 is 0
print(is_div_by_4(24))   # True, because 24 % 4 is 0
print(is_div_by_4(9))    # False, because 9 % 4 is 1
print(is_div_by_4(10))   # False, because 10 % 4 is 2