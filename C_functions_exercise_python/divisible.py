def divisible(num1: int, num2: int) -> bool:
    if num2 == 0:
        return False
    return num1 % num2 == 0

print(divisible(12, 3))    # True
print(divisible(12, 5))    # False
print(divisible(60, 4))    # True
print(divisible(60, 11))   # False
print(divisible(21, 7))    # True
print(divisible(21, 6))    # False