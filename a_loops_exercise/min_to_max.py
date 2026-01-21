# Write a function `min_to_max(min_num, max_num)` that prints all numbers from min to max inclusive.

def min_to_max(min_num, max_num):
    for i in range(min_num, max_num + 1): # this generates numbers from min_num up to (but not including) max_num + 1, which means it includes max_num
        print(i) # each number is printed on its own line


min_to_max(5, 9)
min_to_max(11, 13)
min_to_max(20, 11) # prints nothing because the start value 20 is already past the stop value 11, so the loop body never executes and nothing gets printed

