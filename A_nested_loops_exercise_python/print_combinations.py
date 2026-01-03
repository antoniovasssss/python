def print_combinations(arr1, arr2):
    for item1 in arr1:
        for item2 in arr2:
            print(f"{item1} {item2}")

colors = ["gray", "cream", "cyan"]
clothes = ["shirt", "flannel"]

print_combinations(colors, clothes)