def common_elements(arr1, arr2):
    # convert both lists to sets and find the intersection
    return list(set(arr1) & set(arr2))

print(common_elements(["a", "c", "d", "b"], ["b", "a", "y"]))
print(common_elements([4, 7], [32, 7, 1, 4]))