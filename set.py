#set is an unordered, mutable, unique collection
#set example 
myset = {1, 2, 3, 3, 4}
print(myset)

#no indexing in sets
myset = {10, 20, 30}
# myset[0] ❌ Not allowed

#set manipulation
#add element
myset.add(50)

#update multiple elements
myset.update([60, 70])

#remove element(throws error if missing)
myset.remove(20)

#discard element(safe)
myset.discard(100) #no error

#pop(removes random item)
myset.pop()

#clear set
myset.clear()


#set operations
#set theory operations
#union
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b )


#intersection i.e The operator & keeps only elements that appear in both sets.
print(a & b)
# {3}

#difference
print(a - b)
#{1, 2}

#symmetric difference
print(a ^ b)

