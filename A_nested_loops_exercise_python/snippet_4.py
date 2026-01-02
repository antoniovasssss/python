# Create a list of locations
locations = ["flatbush", "williamsburg", "bushwick", "greenpoint"]

# Outer loop: iterate through each index of the locations list
for i in range(len(locations)):
    # Inner loop: start from the next index (i + 1) to avoid repeating pairs and self-pairs
    for j in range(i + 1, len(locations)):
        # Print the pair of locations at positions i and j
        print(locations[i], locations[j])
