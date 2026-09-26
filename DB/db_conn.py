from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine
import os 


DB_URL = os.getenv("DATABASE_URL")
engine = create_engine(DB_URL)
session = sessionmaker(autoflush=False, autocommit=False, bind=engine)




