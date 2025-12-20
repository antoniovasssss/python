def odd_sum(max_num: int) -> int:
    # handle inputs less than 1, there are no positive odds to add
    if max_num < 1:
        return 0
    # start an accumulator for the running total
    total = 0
    # iterate from 1 up to and including max_num
    for n in range(1, max_num + 1):
    # keep only odd values, an odd gives remainder 1 when divided by 2
        if n % 2 == 1:
            # add the odd number to the total
            total += n
            # return the final sum of all odd numbers in range
    return total

print(odd_sum(10)) # 1 + 3 + 5 + 7 + 9 = 25
print(odd_sum(5)) # 1 + 3 + 5 = 9
print(odd_sum(0)) # 0, no positive odds