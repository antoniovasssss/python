def divisible_range(min_val, max_val, num):
    if num == 0:
        raise ValueError("num must not be zero.")
    # loop through the numbers between min_val and max_val (exclusive)
    for n in range(min_val + 1, max_val):
        if n % num == 0:
            print(n)

divisible_range(17, 40, 9)
divisible_range(10, 24, 4)