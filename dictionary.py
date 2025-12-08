#dictionary in python is an unordered, mutable collection of key value pairs
#dictionary example
student = {
    "name": "Antonio",
    "age": 24,
    "country": "South Africa"
}

#accessing dictionary values
print(student["name"])
print(student["age"])
print(student["country"])

#dictionary is mutable(can change)
#update a value
student["age"] = 25

#dictionary manipution
#add a new key
student["course"] = "Python"

#remove the key
student.pop("age")

#remove the last inserted item
student.popitem()

#delete the key
del student["country"]

#clear dictionary
student.clear()


#dictionary methods
print(student.keys())
print(student.values())
print(student.items())

#update multiple values
student.update({"name": "race", "age": 30})