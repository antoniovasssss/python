def make_matrix(m, n, value):
    return [[value for _ in range(n)] for _ in range(m)]

print(make_matrix(3, 5, None))
print(make_matrix(4, 2, "x"))
print(make_matrix(2, 2, 0))