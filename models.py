from sqlalchemy import Column , Integer , String ,Float
from database import Base
class Products(Base):
    __tablename__="products"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    quantity=Column(Integer,default=0)
    price=Column(Float,nullable=False)


