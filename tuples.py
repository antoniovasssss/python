#nornal tuple 
m = (1, 2, 3)

#tuple with different typles 
info = ("Antonio", 24, "CPT", True)

#single-element tuple 
x = (10,) # comma required

#tuple without parenthesis
t = 1, 2, 3

#Packing & unpacking tuples 

#packing
t = 1, 2, 3

#unpacking
a, b, c = t
print(a, b, c)   # 1 2 3

#extended unpacking 
a, *b = (1, 2, 3, 4, 5)
print(a)  # 1
print(b)  # [2, 3, 4, 5]



#Indexing in tuples
n = (10, 20, 30, 40)

print(n[0])   # 10
print(n[-1])  # 40
print(n[2])   # 30

#slicing tuples 
f = (10, 20, 30, 40, 50)

print(f[1:4])     # (20, 30, 40)
print(f[:3])      # (10, 20, 30)
print(f[::2])     # (10, 30, 50)


#allowed tuple manipulation 
#concatenation
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)
# (1, 2, 3, 4)

#repetition
print((1, 2) * 3)
# (1, 2, 1, 2, 1, 2)

#check if elements exists
t = (1, 2, 3)
print(2 in t)  # True

#count elements 
print((1,2,2,3).count(2))  # 2

#find index 
print((10, 20, 30).index(20))  # 1

# tuple basics
t = (10, 20, 30, 40)

print("First element:", t[0])
print("Slice:", t[1:3])
print("Concatenation:", t + (50, 60))
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))

# unpacking
a, b, c, d = t
print("Unpacked:", a, b, c, d)

#list manipulation
nums.append(50)

#insert
nums.insert(1, 999)

#extend
nums.extend([60, 70])

#remove by value
nums.remove(20)

#pop by index
nums.pop(2)

#delete item
del nums[1]

#clear ist
nums.clear()



#other useful list methods
#sorting
nums.sort()

#reverse
nums.reverse()

#count
nums.count(10)

#index
nums.index(30)

#list comprehension
squares = [x*x for x in range(5)]
print(squares)
# [0, 1, 4, 9, 16]

