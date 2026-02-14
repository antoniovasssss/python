# model methods
from pydantic import BaseModel # imports the BaseModel class from the pydantic library. Pydantic is a data validation library that helps ensure your data has the correct types

class User(BaseModel): # new class called User that inherits from BaseModel. By inheriting from BaseModel, the User class gets automatic data validation and type checking
    name:str
    age:int

    def is_adult(self): # a method called is_adult that belongs to the User class. The self parameter refers to the instance of the class
        return self.age >= 18 # returns true if the users age is 18 or greater otherwise returns false
    
user = User(name="Ant", age=24) # instance of User class with name set to Ant and age to 24. Pydantic automatically validates that these values match the expected types
print(user.is_adult())