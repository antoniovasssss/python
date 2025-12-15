def number_change(n):
    if n % 2 == 0:
        return n // 2
    else:
        return n * 2

# Example checks
print(number_change(6))   # 3
print(number_change(7))   # 14
print(number_change(16))  # 8
print(number_change(21))  # 42