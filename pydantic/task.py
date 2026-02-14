from pydantic import Field, BaseModel
from typing import Optional 

class Student(BaseModel):
    name:str = Field(min_length=3) # ensures the name has at least 3 characters
    roll_no:int = Field(gt=0) # ensures roll number is greater that 0
    email:Optional[str] = None # makes it optional
    marks:int = Field(gt=0, lt=100) # ensures marks are between 0 and 100 (inclusive)

user = Student(name="Ant", roll_no=11, marks=101)
print(user)