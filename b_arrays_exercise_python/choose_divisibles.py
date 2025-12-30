def choose_divisibles(numbers, target):
    # use list ccomprehension to filter numbers divisible by target
    return [num for num in numbers if num % target == 0]

print(choose_divisibles([40, 7, 22, 20, 24], 4))
print(choose_divisibles([9, 33, 8, 17], 3))
print(choose_divisibles([4, 25, 1000], 10))