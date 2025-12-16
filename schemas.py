from pydantic import BaseModel


class Product(BaseModel):
    name:str
    quantity:int
    price:float

    class Config:
        from_attributes = True
