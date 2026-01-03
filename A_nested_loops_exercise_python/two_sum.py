def two_sum(numbers, target):
    seen = set()
    for x in numbers:
        y = target - x # the complement we need 
        if y in seen:
            # found two distinct elements: y (seen earlier) and x (current)
            return True
        seen.add(x)
    return False


print(two_sum([2, 3, 5, 9], 7))   
print(two_sum([2, 3, 5, 9], 4))   
print(two_sum([6, 3, 4], 10))     
print(two_sum([6, 5, 1], 10))     
print(two_sum([5, 5], 10))          
print(two_sum([5], 10))           
