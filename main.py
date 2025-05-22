from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas
from datetime import datetime

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        

@app.post("/clientes/")
def crear_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = models.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

@app.post("/productos/")
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    db_producto = models.Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@app.post("/pedidos/")
def crear_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(get_db)):
    nuevo_pedido = models.Pedido(cliente_id=pedido.cliente_id, fecha=datetime.now())
    db.add(nuevo_pedido)
    db.commit()
    db.refresh(nuevo_pedido)

    for d in pedido.detalles:
        detalle = models.PedidoDetalle(
            pedido_id=nuevo_pedido.id,
            producto_id=d.producto_id,
            cantidad=d.cantidad
        )
        db.add(detalle)
    db.commit()
    return {"pedido_id": nuevo_pedido.id}

@app.get("/")
def read_root():
    return {"message": "API de pedidos funcionando correctamente"}