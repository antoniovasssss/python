# dictionary comprehension
squares = {i: i * i for i in range(1,6)}
print(squares)


# filter dictionary
scores = {
    "Ram": 85,
    "Shym": 72,
    "Harry": 90
}

passed = {name: marks for name, marks in scores.items() if marks >= 80}
print(passed)