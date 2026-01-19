# for n in range(2):
#     print("n=" + str(n))
#     for m in range(5):
#         print("   m=" + str(m))
#     print("n=" + str(n))

for floor in range(1, 4): # outer loop: 3 floors(1,2,3) remember range(1, 2, 3)
    print(f"Floor {floor}")
    for room in range(1, 6): # inner loop: 5 rooms(1,2,3,4,5) remember range(1, 6)
        print(f"  Room {room}")
