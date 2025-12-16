def sum_upto(n):
    if n < 1:
        return 0 
    return n * (n + 1) // 2

print(sum_upto(5))
print(sum_upto(10))