from pydantic import BaseModel
from typing import List
from datetime import datetime

class ClienteCreate(BaseModel):
    nombre: str
    email: str

class ProductoCreate(BaseModel):
    nombre: str
    precio: float

class PedidoDetalleCreate(BaseModel):
    producto_id: int
    cantidad: int

class PedidoCreate(BaseModel):
    cliente_id: int
    detalles: List[PedidoDetalleCreate]
