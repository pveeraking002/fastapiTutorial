from fastapi import FastAPI,Depends
from product import Product 
from sqlalchemy.orm import Session
from DB.db_conn import session,engine
from DB import db_model

db_model.BASE.metadata.create_all(engine)

app = FastAPI(
    title="My Application API",
    swagger_ui_parameters={
        "docExpansion": "none",
    }
)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index(db:Session = Depends(get_db)):
    data = db.query(db_model.Product).all()
    return data


@app.post("/product")
def addProduct(product: Product, db:Session = Depends(get_db)):
    db.add(db_model.Product(**product.model_dump()))
    db.commit()
    return product 

@app.put("/product/{id}")
def updateProduct(id:int, product:Product, db:Session = Depends(get_db)):
    pid = db.query(db_model.Product).filter(db_model.Product.id == id).first()
    if pid:
        pid.name = product.name 
        pid.qty = product.qty
    db.commit()
    return "updated the product"

@app.delete("/product/{id}")
def deleteProduct(id:int,db:Session = Depends(get_db)):
    pid = db.query(db_model.Product).filter(db_model.Product.id == id).first()
    if pid:
        db.delete(pid)
    db.commit()
    return "Product successfully deleted"