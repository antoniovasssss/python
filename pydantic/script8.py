# nested models
from pydantic import BaseModel

class Address(BaseModel):
    city:str
    pin:int

class User(BaseModel):
    name:str
    address:Address # defines an address attribute that must be an instance of the Address class. This creates a nested model, a User contains an Address object

user = User(
    name="Ant",
    address={"city":"Cpt", "pin":11011}
)