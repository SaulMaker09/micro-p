from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from database import Base

class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    email = Column(String(100))

class Producto(Base):
    __tablename__ = "producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    precio = Column(DECIMAL(10,2))

class Pedido(Base):
    __tablename__ = "pedido"
    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey("cliente.id"))
    fecha = Column(DateTime)

class PedidoDetalle(Base):
    __tablename__ = "pedido_detalle"
    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey("pedido.id"))
    producto_id = Column(Integer, ForeignKey("producto.id"))
    cantidad = Column(Integer)
