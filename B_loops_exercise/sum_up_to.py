def sum_up_to(max_num: int) -> int:
    """Return the sum of whole numbers from 1 to max_num inclusive."""
    # Guard for inputs less than 1
    if max_num < 1:
        return 0
    # Start an accumulator at zero
    total = 0
    # Iterate from 1 up to and including max_num
    for n in range(1, max_num + 1):
        total += n # Add each number into total
        # Give the final sum back to the caller
    return total

def sum_up_to_gauss(max_num: int) -> int:
    """Same result using the Gauss formula n*(n+1)//2."""
    # Guard for inputs less than 1
    if max_num < 1:
        return 0 
    # Compute the closed form sum using integer division
    return max_num * (max_num + 1) // 2

# Tiny checks
print(sum_up_to(4))        # 10
print(sum_up_to(5))        # 15
print(sum_up_to(2))        # 3

print(sum_up_to_gauss(4))  # 10
print(sum_up_to_gauss(5))  # 15
print(sum_up_to_gauss(2))  # 3