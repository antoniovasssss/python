def num_odds(numbers):
    # Uses a generator expression inside sum()
    # For each num in numbers, check if num % 2 != 0 (odd)
    # If true, add 1 to the sum
    return sum(1 for num in numbers if num % 2 != 0)


print(num_odds([4, 7, 2, 5, 9]))         
print(num_odds([11, 31, 58, 99, 21, 60])) 
print(num_odds([100, 40, 4]))             
