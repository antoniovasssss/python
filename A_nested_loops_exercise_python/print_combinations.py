# def print_combinations(arr1, arr2):
#     for item1 in arr1:
#         for item2 in arr2:
#             print(f"{item1} {item2}")

# colors = ["gray", "cream", "cyan"]
# clothes = ["shirt", "flannel"]

# print_combinations(colors, clothes)

# Write a function `print_grid(rows, cols)` that accepts two numbers
# and prints a grid pattern with that many rows and columns.
# Each position should show its coordinates.

def print_grid(rows, cols):
    for r in range(rows):
        for c in range(cols):
            print(f"({r},{c})", end=" ")
        print()

print_grid(3, 4)
# Should print:
# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)