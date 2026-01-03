def pair_print(arr):
    # loop over each index i
    for i in range(len(arr)):
        # pair element at i with each element after it (i+1 to end)
        for j in range(i + 1, len(arr)):
            print(f"{arr[i]} - {arr[j]}")

pair_print(["artichoke", "broccoli", "carrot", "daikon"])