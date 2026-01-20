def removes_dupes(lst):
    unique_items = [] # creates an empty list
    for item in lst: # for each item in the input list, checks if its aleady in unique_items
        if item not in unique_items: # if not found, append it to unique_items
            unique_items.append(item)
    return unique_items # returns the deduplicated list

print(removes_dupes(["x", "y", "y", "x", "z"]))
print(removes_dupes([False, False, True, False]))
print(removes_dupes([42, 5, 7, 42, 7, 3, 7, 7]))