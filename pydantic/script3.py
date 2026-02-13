# required vs optional fields
from typing import Optional # optional comes from the typing module 
from pydantic import BaseModel

class User(BaseModel): # creates a new User class that inherits from BaseModel
    name:str
    age:int
    email:Optional[str] =None # means this can be either a string or None, meaning its optional

user = User(name="Antonio", age=24) # creates a User with only name and age, email is not provided becuase its optional
print(user) # prints the user object



# default values
class User(BaseModel):
    name:str
    is_active:bool = True # bool means it must be a boolean (either True or False) but its set to True by default

user = User(name="Antonio")
print(user.is_active)