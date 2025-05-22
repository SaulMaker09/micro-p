from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Reemplaza con tus datos de MySQL
DATABASE_URL = "mysql+mysqlconnector://root:1234@127.0.0.1:3306/pedidos_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
