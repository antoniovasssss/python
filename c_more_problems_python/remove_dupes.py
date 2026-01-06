def removes_dupes(lst):
    unique_items = []
    for item in lst:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

print(removes_dupes(["x", "y", "y", "x", "z"]))
print(removes_dupes([False, False, True, False]))
print(removes_dupes([42, 5, 7, 42, 7, 3, 7, 7]))