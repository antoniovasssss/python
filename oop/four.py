# The __init__() method is a

# special function

# that is used to

# initialize object data.

# In simple words,

# it sets up values

# when an object is created.
class Student:
    def __init__(self): # the __init__ is never called directly, python calls it automatically when an object is created

     print("Student object created")

s1 = Student()




# Using Parameters in __init__()
class Student:
    def __init__(self, name, age): # the self refers to the current object, name and age are params
        self.name = name # data is stored inside the object
        self.age = age

s1 = Student("Ram",20)
s2 = Student("Sita",22)


# Accessing Object Data 
print(s1.name)
print(s2.age)


# Why `__init__()` Matters
# Without `__init__()`:

# - Objects have no data
# - Code becomes messy

# With `__init__()`:

# - Objects are properly initialized
# - Code becomes clean and organized