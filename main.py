from fastapi import FastAPI,Depends,HTTPException
from database import get_db,engine,Base
from sqlalchemy.orm import Session
from models import Products
from schemas import Product
import models
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/product")
def get_all_products(db:Session=Depends(get_db)):
    products=db.query(models.Products).all()
    return products

@app.get("/product/{id}")
def get_products_by_id(id:int,db:Session=Depends(get_db)):
    products=db.query(models.Products).filter(models.Products.id==id).first()
    if not products:
        return {"message":"product not found"}
    return products

@app.post("/product")
def add_products(product:Product,db:Session=Depends(get_db)):
    new_product=Products(
        name=product.name,
        quantity=product.quantity,
        price=product.price
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {"message":"product added successfull"}

@app.put("/product/{id}")
def update_product(id:int,product:Product,db:Session=Depends(get_db)):
    db_Product=db.query(models.Products).filter(models.Products.id==id).first()
    if not db_Product:
        return {"message":"Please enter valid ID"}
    
    db_Product.name=product.name
    db_Product.quantity=product.quantity
    db_Product.price=product.price
    
    db.commit()
    db.refresh(db_Product)
    return {"message":"product updated successfull"}

@app.delete("/product/{id}")
def delete_product(id:int , db:Session=Depends(get_db)):
    product=db.query(Products).filter(Products.id==id).first()

    if product:
        db.delete(product)
        db.commit()
        return {"message":"product deleted"}

    return {"message":"Internal issue"}


