#examples of each data type 

#init
age = 24

#float
price = 7.68

#boolean
is_not_active = False

#string
message = "Hello python"

#list(mutable)
names = ["leonardo", "Donatello", "Rapheal", "Michelangelo"]
names.append("master splinter")

#tuple(immutable)
point = (10, 30)

#dict(mutable)
student = {"name": "dev", "age": 22}
student["age"] = 23

#set(mutable, no dupliates)
unique_numbers = {1, 2, 3, 3, 4}

#frozenset(immutable set)
fs = frozenset([1, 2, 3])

#bytes(immutable)
b = b"hello"

#bytearray(mutable)
ba = bytearray(b"hello")
ba[0] = 72 # H