# Write `countdown(start)`

# Print from start → 1.

def countdown(start):
    for num in range(start, 0, -1): # this generates numbers starting from start, going down to (but not including) 0, decrementing by 1 each time, the -1 is the step value that makes it count backwards
        print(num) # each number is printed on its own line 


countdown(5)