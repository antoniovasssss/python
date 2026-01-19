locations = ["flatbush", "williamsburg", "bushwick", "greenpoint"]


# for i in range(len(locations)):
#     for j in range(i + 1, len(locations)): # the inner loop starts at i + 1 instead of 0, so it only looks at elements after the current one and not choose itself
#         print(locations[i], locations[j])

for x in range(3):
    for y in range(x):
        print(f"x={x}, y={y}")
    print("---")