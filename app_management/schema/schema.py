from pydantic import BaseModel

class UserSchema(BaseModel):
    firstname: str
    name: str
    id: int
    email: str
    password: str
    role: str

class DishSchema(BaseModel):
    dishid: int
    dishname: str
    dishtype: str
    price: str