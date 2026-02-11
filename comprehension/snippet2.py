# tuple comprehension
t = (i * 2 for i in range(1,6))
print(t)
print(type(t))

# correct way to create a tuple
t = tuple(i * 2 for i in range(1,6))
print(t)