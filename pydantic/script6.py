# custom validators
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name:str
    age:int

    @field_validator("age")
    def check_age(cls, value):
        if value < 18:
            raise ValueError("Age must be 18 or older") # this is a logic error, the code only raises an error when it is less than 18 
        return value
        
User(name="Ant", age=11)