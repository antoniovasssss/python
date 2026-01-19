def pair_print(arr):
    for i in range(len(arr)): # outer loop i goes through each index (0,1,2,3)
        for j in range(i + 1, len(arr)): # inner loop j starts at i + 1 and goes to the end
            print(f"{arr[i]} - {arr[j]}")

pair_print(["artichoke", "broccoli", "carrot", "daikon"])
