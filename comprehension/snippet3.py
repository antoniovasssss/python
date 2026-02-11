# set comprehension
numbers = [1,2,2,3,3,4]

unique_numbers = {i for i in numbers}
print(unique_numbers)


# with condition
odd_set = {i for i in range(1,10) if i % 2 != 0} # removing duplicates
print(odd_set)