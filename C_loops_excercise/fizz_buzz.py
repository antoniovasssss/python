def fizz_buzz(max_num):
    # Loop through all numbers from 1 up to max_num (inclusive)
    for num in range(1, max_num + 1):
        # Check if the number is divisible by 3 or 5 but NOT both
        if (num % 3 == 0 or num % 5 == 0) and not (num % 3 == 0 and num % 5 == 0):
            # If condition is true, print the number
            print(num)

fizz_buzz(18) 
fizz_buzz(33) 