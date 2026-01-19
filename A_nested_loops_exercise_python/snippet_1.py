# for i in range(1, 5):
#     for j in range(1, 4):
#         print(i, j)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

for i in list1: # the outer loops value which is 1 will look for the first value of j which is 4
    for j in list2: # this inner loop has to complete befor the outer loop can run again
        print(i, j) # this prints the result i.e 1 4  1 5  1 6...
    print() # this creates a space

# output:
# 1 4
# 1 5
# 1 6
# ...