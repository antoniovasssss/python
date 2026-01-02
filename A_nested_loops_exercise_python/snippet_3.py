# Create a list of friends
friends = ["philip", "abby", "phelipe", "simcha"]

# Outer loop: iterate through each index of the friends list
for i in range(len(friends)):
    # Inner loop: iterate through each index again for pairing
    for j in range(len(friends)):
        # Print the pair of names at positions i and j
        print(friends[i], friends[j])
