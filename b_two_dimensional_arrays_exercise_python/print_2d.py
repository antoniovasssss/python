def print2d(matrix):
    for row in matrix:
        for item in row:
            print(item)

array1 = [
    ["a", "b", "c", "d"],
    ["e", "f"],
    ["g", "h", "i"]
]

print(array1)

array2 = [[9, 3, 4], [11], [42, 100]]
print2d(array2)