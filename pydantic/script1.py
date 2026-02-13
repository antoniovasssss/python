from pydantic import BaseModel # BaseModel is imported from the pydantic library. BaseModel is the foundation you'll use to create your own data models

class User(BaseModel): # class called User that inherits from BaseModel, User class automatically gets all of pydantic's validation 
    name:str
    age:int
    email:str

# using the model
user = User(name="Antonio", age="24", email="antonio@zyx") # here the actual values are passed for each field
print(user)

# automatic type conversion
print(user.age)
print(type(user.age)) # age is made a str but pydantic converts "24" -> 24 a str to int