# email validation 
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name:str # name field is defined
    email:EmailStr # a special string type that validates the value is a properly formatted email address

User(name="Ant", email="antonio@gmail.com")