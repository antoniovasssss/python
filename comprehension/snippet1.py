# list comprehension
numbers = []
for i in range(1,6): # take i from range 1 to 5 
    numbers.append(i * 2) # multiply it by 2

print(numbers)

# with condition
even_numbers = [i for i in range(1,11) if i % 2 == 0] # filtering data, creating results quickly
print(even_numbers)