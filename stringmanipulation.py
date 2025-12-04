#string indexing

s = "PYTHON"

print(s[0])    # P
print(s[3])    # H

print(s[-1])   # N
print(s[-3])   # H

#string slicing
#string[start : end : step]

print(s[0:3])   # PYT   (0,1,2)
print(s[2:5])   # THO   (2,3,4)
print(s[:4])    # PYTH  (from start)
print(s[3:])    # HON   (till end)

#step slicing 

print(s[0:6:2])  # P T O

#reverse using slicing

print(s[::-1])   # NOHTYP

print("hello"[::-1])     # olleh
print("devtech"[::-1])   # hcetved

#more string methods

text = "Hello Python!"

print(text.upper())
# HELLO PYTHON!

print(text.lower())
# hello python!

print(text.capitalize())
# Hello python!

print(text.title())
# Hello Python!

#strip(remove spaces)

msg = "   Python  "
print(msg.strip())
# Python
print(msg.lstrip())
# Python
print(msg.rstrip())
#    Python

#replace

s = "I love Java"
print(s.replace("Java", "Python"))
# I love Python

#split & join

sentence = "apple,banana,mango"
print(sentence.split(","))
# ['apple', 'banana', 'mango']

items = ["a", "b", "c"]
print("-".join(items))
# a-b-c

#find & count

print(text.find("Python"))
# 6

print("banana".count("a"))
# 3


#check methods(boolean methods)

print("Hello".isalpha())
# True

print("12345".isdigit())
# True

print("⑦".isnumeric())
# True (for numeric symbols)

print("Hello123".isalnum())
# True

print("HELLO".isupper())  # True
print("hello".islower())  # True


#encoding & decoding(utf-8)

text = "Hello Python"
encoded = text.encode("utf-8")
print(encoded)
# b'Hello Python'

decoded = encoded.decode("utf-8")
print(decoded)
# Hello Python

msg = "नमस्ते"   # Nepali/Hindi text
enc = msg.encode("utf-8")
print(enc)        # b'\xe0\xa4\xa8...'

dec = enc.decode("utf-8")
print(dec)        # नमस्ते



#startswith() & endswith()

filename = "photo.png"

print(filename.startswith("photo"))  # True
print(filename.endswith(".png"))     # True



#format strings

name = "Antonio"
age = 24
print(f"My name is {name} and I am {age} years old.")

print("Hello, {}".format("Python"))


#reversing a string

s = "Python"
print(s[::-1])
# nohtyP


text = "  I Love Python Programming  "

print(text.upper())
print(text.lower())
print(text.title())
print(text.strip())
print(text.replace("Python", "Java"))
print(text.split())
print("-".join(["A","B","C"]))
print(text.count("o"))
print(text.startswith(" I"))
print(text.endswith("ing"))
print(text.encode("utf-8"))
print(text[::-1])





