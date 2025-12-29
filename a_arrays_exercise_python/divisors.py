def divisors(num):
    # Iterate from 1 to num (inclusive)
    # Check if num % i == 0 (i divides num exactly).
    # Collect all such i in a list.
    return [i for i in range(1, num + 1) if num % i == 0]


print(divisors(15))  
print(divisors(7))   
print(divisors(24))  
