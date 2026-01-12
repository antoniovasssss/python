def is_prime(num):
    # returning false for numbers less than or equal to 1(not prime by definition)
    if num <= 1:
        return False
    # returning true for 2(the only even prime number)
    if num == 2:
        return True
    # returning false for any other even number 
    if num % 2 == 0:
        return False
    
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    
    return True

print(is_prime(11))
print(is_prime(8))
print(is_prime(7))
print(is_prime(21))
print(is_prime(2))
print(is_prime(15))
print(is_prime(1))
