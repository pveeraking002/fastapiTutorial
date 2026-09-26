from fastapi import FastAPI,Depends
from product import Product 
from DB.db_conn import session,engine
from DB import db_model

db_model.BASE.metadata.create_all(engine)

app = FastAPI()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return "working"


@app.post("/product")
def addProduct(product: Product):
    return product 