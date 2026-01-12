def is_prime(num):
    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False
    
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    
    return True

def pick_primes(numbers):
    # creating an empty list to store prime numbers
    primes = []
    # iterating through each number in the input list
    for num in numbers:
        # using the is_prime function to check if each number is prime
        if is_prime(num):
            # adding prime numbers to the result list
            primes.append(num)
    # return the list of primes
    return primes


print(pick_primes([12,3,7,18,11]))

print(pick_primes([17,23,9,42]))

print(pick_primes([4,2048,100,55]))