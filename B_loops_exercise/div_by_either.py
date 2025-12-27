def div_by_either(num1, num2, max_num):
    if num1 == 0 and num2 == 0:
        raise ValueError("At least one of num1 or num2 must be non-zero")
    if max_num <= 1:
        return
    
    for n in range(1, max_num):
        divisible_by_num1 = (num1 != 0 and n % num1 == 0)
        divisible_by_num2 = (num2 != 0 and n % num2 == 0)

        if divisible_by_num1 or divisible_by_num2:
            print(n)

div_by_either(4, 3, 16)