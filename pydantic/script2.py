# validation errors
from pydantic import ValidationError
from pydantic import BaseModel

class User(BaseModel):
    name:str
    age:int


try: # try to run the following code and if an error happens, don't crash the program
    user = User(name="Antonio", age="twentyfour") # User class expects age to be an integer, this will fail validation
except ValidationError as e: # if a validationerror happens in the try block, catch it and store it in a variable called e, prevents the program from crashing and lets us handle the error gracefully
    print(e)