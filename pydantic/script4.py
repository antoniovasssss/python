# field contraints
from pydantic import Field, BaseModel # field - a function that lets you add extra validation rules and constrains to your fields

class User(BaseModel):
    name:str = Field(min_length=3, max_length=20)
    age:int = Field(gt=0, lt=120)

User(name="An", age=-5)